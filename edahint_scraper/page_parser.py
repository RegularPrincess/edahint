from bs4 import BeautifulSoup as bs
from product import Product
import re


def _pars_foto_link(div):
    filthy_link_foto = div.attrs['style']
    foto_link = filthy_link_foto.split('"')[1]
    return foto_link


def _pars_date_end(div):
    return div.text


def _pars_price(div):
    text = div.text
    digits = ''
    for c in text:
        if c in ('0','1','2','3','4','5','6','7','8','9',','):
            digits += c
    return float(digits.replace(',', '.'))


def _pars_store(div):
    return div.attrs['title']


def _pars_name(div):
    return div.text


def _pars_prod(item):
    foto_link = _pars_foto_link(item.find('div', class_='b-offer__preview'))
    date_end = _pars_date_end(item.find('div', class_='b-offer__dates'))
    price = _pars_price(item.find('div', class_='b-offer__price-new'))
    store = _pars_store(item.find('img', class_='b-offer__retailer-icon'))
    name = _pars_name(item.find('div', class_='b-offer__description'))
    return Product(name=name, foto_link=foto_link, date_end=date_end, price=price, store=store)


def delete_special_character(obj):
    reg = re.compile('[^\w.,-: %()\"\']')
    obj.name_prod = reg.sub(' ', obj.name_prod).lower()
    obj.date_end = reg.sub(' ', obj.date_end)
    obj.store = obj.store.lower()


def pars_page(html):
    #отдаем чтмл страницу библиотеке бьютифул суп
    soup = bs(html, 'html.parser')
    products_no_pars = soup.findAll('a', class_='p-offers__offer')
    products = []
    for item in products_no_pars:
        prod = _pars_prod(item)
        #Убирает все не буквы не цифры и не некоторые символы
        delete_special_character(prod)
        products.append(prod)
    return products