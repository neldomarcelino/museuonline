from flask import Blueprint, request, session, render_template, url_for
from werkzeug.utils import redirect

from src.models.Regiao.regiao import Regiao

regiao_blueprint = Blueprint('regiao', __name__)


@regiao_blueprint.route('/add', methods=['POST','GET'])
def regiao_add():
    if request.method == 'POST':
        regiao = request.form['regiao']
        if Regiao(regiao).insert():
            return redirect(url_for(".regioes"))

    return render_template("regiao/register_regiao.html")


@regiao_blueprint.route('/mostra')
def regioes():
    data = Regiao.find_all()
    return render_template("regiao/regioes.html", data=data)


@regiao_blueprint.route('/delete/<string:idregiao>')
def delete_regiao(idregiao):

    reino = Regiao.find_by_id(idregiao)
    if reino is not None:
        Regiao.delete(idregiao)

    return redirect(url_for(".regioes"))


@regiao_blueprint.route('/edit/<string:idregiao>', methods=['POST', 'GET'])
def edit_regiao(idregiao=None):

    regiao = Regiao.find_by_id(idregiao)
    if regiao is not None:

        if request.method == 'POST':
            regiao_form = request.form['regiao']
            Regiao.editar(idregiao, regiao_form)
            return redirect(url_for(".regioes"))

        return render_template("regiao/edit_regiao.html", regiao=regiao[1])

    return redirect(url_for(".regioes"))

