class Product:
    """Class for representation product"""

    def __init__(self, name, price, date_end, foto_link, store):
        self.name_prod = name
        self.price = price
        self.date_end = date_end
        self.foto_link = foto_link
        self.store = store
        self.id = -1

    def __str__(self):
        return str(self.name)