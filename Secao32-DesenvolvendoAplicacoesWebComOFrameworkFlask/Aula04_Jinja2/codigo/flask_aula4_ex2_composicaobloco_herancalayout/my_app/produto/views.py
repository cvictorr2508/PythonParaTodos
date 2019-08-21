from werkzeug import abort
from flask import render_template
from flask import Blueprint
from my_app.produto.models import PRODUTOS

product_blueprint = Blueprint('produto', __name__)

@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
    return render_template('home.html', produtos=PRODUTOS)

@product_blueprint.route('/produto/<key>')
def produto(key):
    produto = PRODUTOS.get(key)
    if not produto:
        return render_template('erro.html')
    return render_template('produto.html', produto=produto)
