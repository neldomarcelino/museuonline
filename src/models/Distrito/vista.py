from flask import Blueprint, request, session, render_template, url_for
from werkzeug.utils import redirect

from src.models.Provincia.provincia import Provincia
from src.models.Distrito.distrito import Distrito

distrito_blueprint = Blueprint('distrito', __name__)


@distrito_blueprint.route('/add', methods=['POST','GET'])
def distrito_add():
    if request.method == 'POST':
        distrito = request.form['distrito']
        idprovincia = request.form['provincia']
        if Distrito(distrito, idprovincia).insert():
            return redirect(url_for(".distritos"))
    data = Provincia.find_all()
    return render_template("distrito/register_distrito.html", data=data)


@distrito_blueprint.route('/mostra')
def distritos():
    data = Distrito.find_all()
    return render_template("distrito/distritos.html", data=data)


@distrito_blueprint.route('/delete/<string:iddistrito>')
def delete_distrito(iddistrito):
    distrito = Distrito.find_by_id(iddistrito)
    if distrito is not None:
        Distrito.delete(iddistrito)

    return redirect(url_for(".distritos"))


@distrito_blueprint.route('/edit/<string:iddistrito>', methods=['POST', 'GET'])
def edit_distrito(iddistrito=None):

    distrito = Distrito.find_by_id(iddistrito)
    if distrito is not None:

        if request.method == 'POST':
            distrito_form = request.form['distrito']
            Distrito.editar(iddistrito, distrito_form)
            return redirect(url_for(".distritos"))

        return render_template("distrito/edit_distrito.html", distrito=distrito[1])

    return redirect(url_for(".distritos"))

