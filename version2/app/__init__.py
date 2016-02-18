from flask import Flask

app = Flask(__name__)

app.config["DATABASE"] = 'names.db'
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = "restful web services kpmg"
app.config["USERNAME"] = "Carlo"
app.config["PASSWORD"] = "Butelli"

from app import views, modules
