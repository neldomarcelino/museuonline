from flask import Blueprint, request, session, render_template, url_for
from werkzeug.utils import redirect

from src.models.Pessoa.pessoa import Pessoa

reino_blueprint = Blueprint('reino', __name__)


@reino_blueprint.route('/add', methods=['POST','GET'])
def pessoa_add():
    if request.method == 'POST':
        nome = request.form['nome']
        if Pessoa(nome).insert():
            return redirect(url_for(".pessoas"))

    return render_template("pessoa/register_pessoa.html")


@reino_blueprint.route('/mostra')
def pessoas():
    data = Pessoa.find_all()
    return render_template("pessoa/pessoas.html", data=data)


@reino_blueprint.route('/delete/<string:idpessoa>')
def delete_pessoa(idpessoa):
    pessoa = Pessoa.find_by_id(idpessoa)
    if pessoa is not None:
        Pessoa.delete(idpessoa)

    return redirect(url_for(".pessoas"))


@reino_blueprint.route('/edit/<string:idpessoa>', methods=['POST', 'GET'])
def edit_pessoa(idpessoa=None):

    pessoa = Pessoa.find_by_id(idpessoa)
    if pessoa is not None:

        if request.method == 'POST':
            pessoa_form = request.form['pessoa']
            Pessoa.editar(idpessoa, pessoa_form)
            return redirect(url_for(".pessoas"))

        return render_template("pessoa/edit_pessoa.html", pessoa=pessoa[1])

    return redirect(url_for(".pessoas"))


