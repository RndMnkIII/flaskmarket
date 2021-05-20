from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import locale


### Se utiliza para conversión de características locales: separador de miles, decimales, moneda, ...
#locale.setlocale(locale.LC_ALL, '')
# Establecer configuración para España en Ubuntu
locale.setlocale(locale.LC_ALL, 'es_ES.UTF8')  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = os.urandom(12).hex()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = 'info'

from market import routes
