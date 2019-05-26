
from flask import Blueprint, request, session, render_template, url_for, Response
from werkzeug.utils import redirect

from src import config
from src.models.Utilizador.utilizador import Utilizador
from src.models.TipoUtilizador.tipoUtilizador import TipoUtilizador
from src.models.Utilizador.decorators import login_required_admin
import xml.etree.cElementTree as txml

utilizador_blueprint = Blueprint('utilizador', __name__)


@utilizador_blueprint.route('/login', methods=['POST','GET'])
def login_user():
    message = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']


        if Utilizador.is_login_valid(email, password):
            session['email'] = email
            return redirect(url_for("especie.especies"))
        else:
            message = "Erro: Verrfique o Email ou Password!!"

    return render_template("utilizador/login.html", message=message)


@utilizador_blueprint.route('/register/<string:admin>', methods=['GET', 'POST'])
def register_user(admin=None):
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if session['email'] in config.ADMINS:
            #tipo_utilizador = request.form['tipoutilizador']
            tipo_utilizador = "7"
            if Utilizador(email, password, tipo_utilizador).register():
                return redirect(url_for(".utilizadores"))
        else:
            tipo_utilizador = "7"
            if Utilizador(email, password, tipo_utilizador).register():
                return redirect(url_for(".login_user"))

    data = TipoUtilizador.find_all()
    return render_template("utilizador/register.html", data=data, admin=admin)


@utilizador_blueprint.route("/lista_utilizadores")
@login_required_admin
def utilizadores():
    data = Utilizador.find_all()
    return render_template("utilizador/lista_usuarios.html", usuarios=data)


@utilizador_blueprint.route("/delete_utilizador/<string:id_utilizador>", methods=['POST','GET'])
@login_required_admin
def delete_utilizador(id_utilizador=None):
    utilizador = Utilizador.find_by_id(id_utilizador)
    if utilizador is not None:
        Utilizador.delete(id_utilizador)

    data = Utilizador.find_all()
    return render_template("utilizador/lista_usuarios.html", usuarios=data)


@utilizador_blueprint.route('/logout')
def logout():
    session['email'] = None
    return redirect(url_for("especie.especies"))


@utilizador_blueprint.route("/recuperar_password/<string:email>", methods=['POST', 'GET'])
def recuperar_password(email=None):
    message = " Email nao existe!!"
    print(email)
    if request.method == 'GET':
        #email = request.form['email']
        utilizador = Utilizador.find_by_email(email)
        if utilizador is not None:
            result = Utilizador.recuperar_password(utilizador)
            if result is not None:
                message = result
            else:
                message += " Verfique no email a palavra passe"

    return render_template("utilizador/login.html", message=message)


@utilizador_blueprint.route('/pesquisa/<string:email>', methods=['POST'])
def pesquisa_especie(email=None):

    if email == "-*.M21":
        utilizadores_p = Utilizador.find_all()
    else:
        utilizadores_p = Utilizador.find_pesquisa(email)

    cabeca = txml.Element('utilizadores')

    for (idutilizador, email, password, idtipo) in utilizadores_p:

            element = txml.SubElement(cabeca, 'c_utilizador')
            elemento1 = txml.SubElement(element,'idutilizador')
            elemento2 = txml.SubElement(element,'email')
            elemento3 = txml.SubElement(element,'password')
            elemento4 = txml.SubElement(element,'idtipo')

            elemento1.text = "{}".format(idutilizador)
            elemento2.text = "{}".format(email)
            elemento3.text = "{}".format(password)
            elemento4.text = "{}".format(idtipo)

    my_xml = txml.tostring(cabeca)

    b = Response()
    b.set_data(my_xml)
    b.status = "200"
    b.get_json(force=False, silent=True, cache=True)
    b.mimetype = "application/xml"
    return b.get_data()
