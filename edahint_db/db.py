import psycopg2


class db:

    __instance = None

    @staticmethod
    def get_inst():
        # Синглтон. Получать экземпляр с помощью этого метода
        if db.__instance is None:
            db.__instance = db()
            return db.__instance
        else:
            return db.__instance

    def __init__(self):
        print('Connecting...')
        self.__conn = psycopg2.connect(dbname='edahint', user='postgres', host='localhost', password='postgres')
        # conn_str = (
        #     "DRIVER={PostgreSQL Unicode};"
        #     "DATABASE=edahint;"
        #     "UID=postgres;"
        #     "PWD=postgres;"
        #     "SERVER=localhost;"
        #     "PORT=5432;"
        #     )
        # self.__conn = pyodbc.connect(conn_str)
        self.cursor = self.__conn.cursor()
        print('Connected!')
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS prods (
            id SERIAL PRIMARY KEY,
            name_prod VARCHAR(255),
            price VARCHAR(127),
            date_end VARCHAR(127),
            foto_link VARCHAR(255),
            store VARCHAR(127));""")

    def __del__(self):
        self.cursor.close()
        self.__conn.close()

    def insert(self, prod_dict):
        # Принимает обьект в виде словаря (поле : значение)
        sql = """INSERT INTO prods (name_prod, price, date_end, foto_link, store) VALUES 
                  (%(name_prod)s, %(price)s, %(date_end)s, %(foto_link)s, %(store)s);"""
        self.cursor.execute(sql, prod_dict)
        self.__conn.commit()

    def get_permanent_data(self):
        # Возвращает список полей продукта в виде tuple
        self.cursor.execute('select * from prods;')
        row_data = self.cursor.fetchall()
        return row_data



