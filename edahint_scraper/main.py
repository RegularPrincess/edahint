import os
import page_parser
import scraper
from edahint_db.db import db


db = db.get_inst()
files = os.listdir('data')
for file in files:
    page = scraper.get_local_page('data/' + file)
    prods = page_parser.pars_page(page)
    for prod in prods:
        db.insert(prod.__dict__)
