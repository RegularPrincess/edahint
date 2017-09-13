import os
import page_parser
import scraper
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from edahint_db.db import db


db = db.get_inst()
files = os.listdir('data')
for file in files:
    page = scraper.get_local_page('data/' + file)
    prods = page_parser.pars_page(page)
    for prod in prods:
        db.insert(prod.__dict__)
