from flask import Blueprint, request, session, render_template, url_for
from werkzeug.utils import redirect

from src.models.MetodoPreservacao.metodoPreservacao import MetodoPreservacao


reino_blueprint = Blueprint('reino', __name__)


@reino_blueprint.route('/add', methods=['POST','GET'])
def metodo_add():
    if request.method == 'POST':
        metodo = request.form['metodo']
        if MetodoPreservacao(metodo).insert():
            return redirect(url_for(".metodos"))

    return render_template("metodo/register_metodo.html")


@reino_blueprint.route('/mostra')
def metodos():
    data = MetodoPreservacao.find_all()
    return render_template("metodo/metodos.html", data=data)


@reino_blueprint.route('/delete/<string:idmetodo>')
def delete_metodo(idmetodo):
    metodo = MetodoPreservacao.find_by_id(idmetodo)
    if metodo is not None:
        MetodoPreservacao.delete(idmetodo)

    return redirect(url_for(".metodos"))


@reino_blueprint.route('/edit/<string:idmetodo>', methods=['POST', 'GET'])
def edit_metodo(idmetodo=None):

    metodo = MetodoPreservacao.find_by_id(idmetodo)
    if metodo is not None:

        if request.method == 'POST':
            metodo_form = request.form['metodo']
            MetodoPreservacao.editar(idmetodo, metodo_form)
            return redirect(url_for(".metodos"))

        return render_template("metodo/edit_metodo.html", metodo=metodo[1])

    return redirect(url_for(".metodos"))

