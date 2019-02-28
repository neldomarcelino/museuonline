from flask import Blueprint, request, session, render_template, url_for
from werkzeug.utils import redirect

from src.models.Filo.filo import Filo
from src.models.Reino.reino import Reino

filo_blueprint = Blueprint('filo', __name__)


@filo_blueprint.route('/add', methods=['POST','GET'])
def filo_add():
    if request.method == 'POST':
        filo = request.form['filo']
        idreino = request.form['reino']
        if Filo(filo,idreino).insert():
            print(idreino)
            return redirect(url_for(".filos"))
    reinos = Reino.find_all()
    return render_template("filo/register_filo.html", reinos = reinos)


@filo_blueprint.route('/mostra')
def filos():
    data = Filo.find_all()
    reino = Reino.find_all()
    return render_template("filo/filos.html", data=data, reino=reino)


@filo_blueprint.route('/delete/<string:idfilo>')
def delete_filo(idfilo):
    if session['email'] is not None:
        filo = Filo.find_by_id(idfilo)
        if filo is not None:
            Filo.delete(idfilo)

    return redirect(url_for(".filos"))


@filo_blueprint.route('/edit/<string:idfilo>', methods=['POST', 'GET'])
def edit_filo(idfilo=None):

    filo = Filo.find_by_id(idfilo)
    if filo is not None:

        if request.method == 'POST':
            filo_form = request.form['filo']
            Filo.editar(idfilo, filo_form)
            return redirect(url_for(".filos"))

        return render_template("filo/edit_filo.html", filo=filo[1])

    return redirect(url_for(".filos"))
