from flask import Blueprint, request, session, render_template, url_for
from werkzeug.utils import redirect

from src.models.Provincia.provincia import Provincia
from src.models.Regiao.regiao import Regiao

provincia_blueprint = Blueprint('provincia', __name__)


@provincia_blueprint.route('/add', methods=['POST','GET'])
def provincia_add():
    if request.method == 'POST':
        provincia = request.form['provincia']
        idregiao = request.form['regiao']
        if Provincia(provincia, idregiao).insert():
            return redirect(url_for(".provincias"))
    data = Regiao.find_all()
    return render_template("provincia/register_provincia.html", data=data)


@provincia_blueprint.route('/mostra')
def provincias():
    data = Provincia.find_all()
    return render_template("provincia/provincias.html", data=data)


@provincia_blueprint.route('/delete/<string:idprovincia>')
def delete_provincia(idprovincia):
    provincia = Provincia.find_by_id(idprovincia)
    if provincia is not None:
        Provincia.delete(idprovincia)

    return redirect(url_for(".provincias"))


@provincia_blueprint.route('/edit/<string:idprovincia>', methods=['POST', 'GET'])
def edit_provincia(idprovincia=None):

    provincia = Provincia.find_by_id(idprovincia)
    if provincia is not None:

        if request.method == 'POST':
            provincia_form = request.form['provincia']
            Provincia.editar(idprovincia, provincia_form)
            return redirect(url_for(".provincias"))

        return render_template("provincia/edit_provincia.html", provincia=provincia[1])

    return redirect(url_for(".provincias"))

