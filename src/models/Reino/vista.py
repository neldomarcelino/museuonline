from flask import Blueprint, request, session, render_template, url_for, Response
from werkzeug import http
from werkzeug.utils import redirect

from src.models.Reino.reino import Reino
from src.models.Filo.filo import Filo
from src.models.Utilizador.decorators import login_required_admin

reino_blueprint = Blueprint('reino', __name__)


@reino_blueprint.route('/add', methods=['POST','GET'])
@login_required_admin
def reino_add():
    if request.method == "POST":
        reino = request.form['reino']
        if Reino(reino).insert():
            return redirect(url_for(".reinos"))

    return render_template("reino/register_reino.html")


@reino_blueprint.route('/mostra')
def reinos():
    data = Reino.find_all()
    return render_template("reino/reinos.html", data=data)


@reino_blueprint.route('/delete/<string:idreino>', methods=['POST'])
@login_required_admin
def delete_reino(idreino):
    reino = Reino.find_by_id(idreino)
    if reino is not None:
        Reino.delete(idreino)

    b = Response()
    b.set_data("apagado id= {}".format(idreino))
    b.status = "200"
    b.get_json(force=False, silent=True, cache=True)
    b.mimetype = "application/xml"
    return b.get_data()


@reino_blueprint.route('/edit/<string:idreino>', methods=['POST', 'GET'])
@login_required_admin
def edit_reino(idreino=None):
    reino = Reino.find_by_id(idreino)
    if reino is not None:

        if request.method == 'POST':
            reino_form = request.form['reino']
            Reino.editar(idreino, reino_form)
            return redirect(url_for(".reinos"))

        return render_template("reino/edit_reino.html", reino=reino[1])

    return redirect(url_for(".reinos"))


@reino_blueprint.route('/reinoseacher/<string:seacher>')
def reinoseacher(seacher):

    busca = Filo.buscar_reino(seacher)

    if busca is not None:
        return render_template("reino/reino_detalhe.html", data=busca, reino=seacher)
    return render_template("reino/reinos.html")