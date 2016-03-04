from flask import Flask
from flask.ext.cache import Cache

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)

app.config["DATABASE"] = 'names.db'
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = "restful web services kpmg"
app.config["USERNAME"] = "Carlo"
app.config["PASSWORD"] = "Butelli"

from app import views, modules
