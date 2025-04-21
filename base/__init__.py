import warnings
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.secret_key = 'qazwsxedcrfvtgbyhnujmiklop123456'

app.config['SQLALCHEMY_ECHO'] = True



app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://quickmart_user:8bFtIGpJCGBa3WosNW3DllH5lB2zl42a@dpg-d02fsaeuk2gs73eekk70-a/quickmart'

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0
app.app_context().push()
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from base.com import controller
