import pymssql


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
        # self.__conn = pymssql.connect(server='my-edadeal.database.windows.net', user='my-edadeal@my-edadeal',
        #                        password='piknikME000', database='my-edadeal    ')
        self.__conn = pymssql.connect(server='localhost', port=5432, user='postgres', password='postgres', database='edahint')
        self.cursor = self.__conn.cursor()
        print('Connected!')

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



