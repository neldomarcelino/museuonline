from flask import Blueprint, request, session, render_template, url_for
from werkzeug.utils import redirect

from src.models.Ordem.ordem import Ordem
from src.models.Familia.familia import Familia

familia_blueprint = Blueprint('familia', __name__)


@familia_blueprint.route('/add', methods=['POST','GET'])
def familia_add():
    if request.method == 'POST':
        familia = request.form['familia']
        idordem = request.form['ordem']
        if Familia(familia, idordem).insert():
            return redirect(url_for(".familias"))
    ordem = Ordem.find_all()
    return render_template("familia/register_familia.html", ordems=ordem)


@familia_blueprint.route('/mostra')
def familias():
    data = Familia.find_all()
    return render_template("familia/familias.html", data=data)


@familia_blueprint.route('/delete/<string:idfamilia>')
def delete_familia(idfamilia):
    familia = Familia.find_by_id(idfamilia)
    if familia is not None:
        Familia.delete(idfamilia)

    return redirect(url_for(".familias"))


@familia_blueprint.route('/edit/<string:idfamilia>', methods=['POST', 'GET'])
def edit_familia(idfamilia=None):

    familia = Familia.find_by_id(idfamilia)
    if familia is not None:

        if request.method == 'POST':
            familia_form = request.form['familia']
            Familia.editar(idfamilia, familia_form)
            return redirect(url_for(".familias"))

        return render_template("familia/edit_familia.html", familia=familia[1])

    return redirect(url_for(".familias"))
