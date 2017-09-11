from edahint_db import db


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
    # возвращает список предложенных продуктов
    global _data
    if _data is None:
        tuple_data = db.get_inst().get_permanent_data()
        for t in tuple_data:
            _data.append(Product(t))

    selected_prods = []
    for obj in list:
        matches = search_all_match(obj)
        if len(matches) == 0:
            continue
        if price_category is 'low':
            selected_prods.append(low_price_prod(matches))
    return selected_prods
