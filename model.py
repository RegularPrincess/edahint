import pymssql as mysql


_connection = None
_cursor = None
_data = None


class Product:
    """Class for representation product"""

    def __init__(self, toupl):
        self.name_prod = toupl[1]
        self.price = toupl[2]
        self.date_end = toupl[3]
        self.foto_link = toupl[4]
        self.store = toupl[5]
        self.id = toupl[0]

    def __str__(self):
        return str(self.name)


def _connect():
    global _connection, _cursor
    _connection = mysql.connect(host="my-edadeal.database.windows.net", user='my-edadeal@my-edadeal',
                                  password='piknikME000', database='my-edadeal')
    _cursor = _connection.cursor()
    print("Connected!!!!!")
    # _cursor.execute("SET CHARACTER SET 'utf8'")
    # _cursor.execute("SET SESSION collation_connection = 'utf8_general_ci'")


def _get_permanent_data():
    global _connection, _cursor, _data
    if _connection is None:
        _connect()
    _data = []
    _cursor.execute('select * from prods;')
    row_data = _cursor.fetchall()
    for x in row_data:
        _data.append(Product(x))


def _close():
    global _connection, _cursor
    _connection.close()
    _cursor.close()


def search_all_match(obj):
    global _data
    matches = []
    for d in _data:
        if obj in d.name_prod:
            matches.append(d)
    return matches


def low_price_prod(matches):
    min_price = matches[0].price
    selected_prod = matches[0]
    for match in matches:
        if min_price > match.price:
            min_price = match.price
            selected_prod = match
    return selected_prod


def compute_hint(list, price_category):
    global _connection, _cursor, _data
    if _data is None:
        _get_permanent_data()
    selected_prods = []
    for obj in list:
        matches = search_all_match(obj)
        if len(matches) == 0:
            continue
        if price_category is 'low':
            selected_prods.append(low_price_prod(matches))
    return selected_prods


def get_separate_data(substr):
    if _connection is None:
        _connect()
    print('SELECT * FROM prods WHERE name_prod LIKE \'%' + substr + '%\';')
    _cursor.execute('SELECT * FROM prods WHERE name_prod LIKE \'%' + substr + '%\';')
    print(_cursor.fetchone())