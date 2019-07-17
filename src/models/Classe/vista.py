from flask import Blueprint, request, session, render_template, url_for
from werkzeug.utils import redirect

from src.models.Classe.classe import Classe
from src.models.Filo.filo import Filo
from src.models.Reino.reino import Reino

classe_blueprint = Blueprint('classe', __name__)
from src.models.Utilizador.decorators import login_required_user, login_required_admin


@classe_blueprint.route('/add', methods=['POST', 'GET'])
@login_required_admin
def classe_add():
    if request.method == 'POST':
        classe = request.form['classe']
        idfilo = request.form['filo']
        if Classe(classe, idfilo).insert():
            return redirect(url_for(".classes"))
    filos = Filo.find_all()
    reinos = Reino.find_all()
    return render_template("classe/register_classe.html", reinos=reinos, filos=filos)


@classe_blueprint.route('/mostra')
def classes():
    data = Classe.find_all()
    return render_template("classe/classes.html", data=data)


@classe_blueprint.route('/delete/<string:idclasse>')
@login_required_admin
def delete_classe(idclasse):
    classe = Classe.find_by_id(idclasse)
    if classe is not None:
        Classe.delete(idclasse)

    return redirect(url_for(".classes"))


@classe_blueprint.route('/edit/<string:idclasse>', methods=['POST', 'GET'])
@login_required_admin
def edit_classe(idclasse=None):
    classe = Classe.find_by_id(idclasse)
    if classe is not None:

        if request.method == 'POST':
            classe_form = request.form['classe']
            Classe.editar(idclasse, classe_form)
            return redirect(url_for(".classes"))

        return render_template("classe/edit_classe.html", classe=classe[1])

    return redirect(url_for(".classes"))
