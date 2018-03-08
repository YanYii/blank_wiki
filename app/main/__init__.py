from flask import Blueprint

main = Blueprint('main', __name__)

# 必要
from . import views
