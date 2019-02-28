from flask import Blueprint, request, session, render_template, url_for
from werkzeug.utils import redirect

from src.models.Familia.familia import Familia
from src.models.Genero.genero import Genero
genero_blueprint = Blueprint('genero', __name__)


@genero_blueprint.route('/add', methods=['POST','GET'])
def genero_add():
    if request.method == 'POST':
        genero = request.form['genero']
        idfamilia = request.form['familia']
        if Genero(genero, idfamilia).insert():
            return redirect(url_for(".generos"))
    familia = Familia.find_all()
    return render_template("genero/register_genero.html", familias=familia)


@genero_blueprint.route('/mostra')
def generos():
    data = Genero.find_all()
    return render_template("genero/generos.html", data=data)


@genero_blueprint.route('/delete/<string:idgenero>')
def delete_genero(idgenero):
    genero = Genero.find_by_id(idgenero)
    if genero is not None:
        Genero.delete(idgenero)

    return redirect(url_for(".generos"))


@genero_blueprint.route('/edit/<string:idgenero>', methods=['POST', 'GET'])
def edit_genero(idgenero=None):

    genero = Genero.find_by_id(idgenero)
    if genero is not None:

        if request.method == 'POST':
            genero_form = request.form['genero']
            Genero.editar(idgenero, genero_form)
            return redirect(url_for(".generos"))

        return render_template("genero/edit_genero.html", genero=genero[1])

    return redirect(url_for(".generos"))
