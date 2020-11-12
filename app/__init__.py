from flask import Flask
from config import TestingConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
app.config.from_object(TestingConfig)
Bootstrap(app)
db = SQLAlchemy(app)
moment = Moment(app)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

from app.views import *