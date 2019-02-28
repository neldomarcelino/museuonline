from flask import Blueprint, request, session, render_template, url_for
from werkzeug.utils import redirect

from src.models.Ordem.ordem import Ordem
from src.models.Classe.classe import Classe

ordem_blueprint = Blueprint('ordem', __name__)


@ordem_blueprint.route('/add', methods=['POST','GET'])
def ordem_add():
    if request.method == 'POST':
        ordem = request.form['ordem']
        idclasse = request.form['classe']
        if Ordem(ordem, idclasse).insert():
            return redirect(url_for(".ordems"))
    classe = Classe.find_all()
    return render_template("ordem/register_ordem.html", classes=classe)


@ordem_blueprint.route('/mostra')
def ordems():
    data = Ordem.find_all()
    return render_template("ordem/ordems.html", data=data)


@ordem_blueprint.route('/delete/<string:idordem>')
def delete_ordem(idordem):
    ordem = Ordem.find_by_id(idordem)
    if ordem is not None:
        Ordem.delete(idordem)

    return redirect(url_for(".ordems"))


@ordem_blueprint.route('/edit/<string:idordem>', methods=['POST', 'GET'])
def edit_ordem(idordem=None):

    ordem = Ordem.find_by_id(idordem)
    if ordem is not None:

        if request.method == 'POST':
            ordem_form = request.form['ordem']
            Ordem.editar(idordem, ordem_form)
            return redirect(url_for(".ordems"))

        return render_template("ordem/edit_ordem.html", ordem=ordem[1])

    return redirect(url_for(".ordems"))
