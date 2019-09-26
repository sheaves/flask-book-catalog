# app\catalog\__init.py__
from flask import Blueprint

main = Blueprint('main', __name__, template_folder = 'templates')

# imported at the bottom instead of at the top, to avoid circular dependencies
# (routes imports main from here)
from app.catalog import routes