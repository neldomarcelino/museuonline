from flask import Blueprint, request, session, render_template, url_for, make_response, Response
from werkzeug.utils import redirect, secure_filename
import datetime
import xml.etree.cElementTree as txml

from src.models.Utilizador.decorators import login_required
from src.models.Especie.especie import Especie
from src.models.Genero.genero import Genero
from src.models.QuemIdentificou.quemIdentificou import QuemIdentificou
from src.models.QuemEncontrou.quemEncontrou import QuemEncontrou
from src.models.Pessoa.pessoa import Pessoa
from src.models.PreservacaoEspecie.preservacaoEspecie import PreservacaoEspecie
from src.models.LocalizacaoEspecie.localizacaoEspecie import LocalizacaoEspecie
from src.models.Imagem.imagem import Imagem

especie_blueprint = Blueprint('especie', __name__)


@especie_blueprint.route('/add', methods=['POST', 'GET'])
def especie_add():
    if request.method == 'POST':
        especie = request.form['especie']
        genero = request.form['genero']
        habitat = request.form['habitat']
        coordenadas = request.form['coordenadas']
        notas = request.form['notas']
        detalhes = request.form['detalhes']
        nomecomum = request.form['nomecomum']
        validacao = request.form['validacao']
        datacriacao = datetime.datetime.utcnow()

        codigo = Especie(especie, genero, habitat, coordenadas, notas, detalhes, nomecomum, validacao,
                         datacriacao).insert()
        idespecie = Especie.find_by_codigo(codigo)

        return redirect(url_for(".quem_encon_identf", idespecie=idespecie))

    genero = Genero.find_all()
    return render_template("especie/register_especie.html", generos=genero)


@especie_blueprint.route('/quem_encon_identf/<string:idespecie>', methods=['POST', 'GET'])
def quem_encon_identf(idespecie=None):
    if request.method == 'POST':
        encontrou = request.form['pessoa_encontrou']
        identificou = request.form['pessoa_identifico']
        QuemEncontrou(encontrou, idespecie).insert()
        QuemIdentificou(identificou, idespecie).insert()
        metodo = request.form['metodo']
        distrito = request.form['distrito']
        LocalizacaoEspecie(distrito, idespecie).insert()
        PreservacaoEspecie(idespecie, metodo).insert()

        return redirect(url_for(".imagem_especie", idespecie=idespecie))

    pessoas = Pessoa.find_all()
    return render_template('especie/register_quem.html', pessoas=pessoas, idespecie=idespecie)


@especie_blueprint.route('/metodo_preservacao/<string:idespecie>', methods=['POST', 'GET'])
def metodo_preservacao(idespecie=None):
    if request.method == 'POST':
        metodo = request.form['metodo']
        distrito = request.form['distrito']
        LocalizacaoEspecie(distrito, idespecie).insert()
        PreservacaoEspecie(idespecie, metodo).insert()
        return redirect(url_for(".imagem_especie", idespecie=idespecie))

    pessoas = Pessoa.find_all()
    return render_template('especie/metodo_preservacao.html', pessoas=pessoas, idespecie=idespecie)


@especie_blueprint.route('/imagem_especie/<string:idespecie>', methods=['POST', 'GET'])
def imagem_especie(idespecie=None):
    if request.method == 'POST':
        imagem = request.files['file_t']
        Imagem.imagem_processamento(imagem, idespecie)

        return redirect(url_for(".especie_completa", idespecie=idespecie))
    return render_template("especie/multimedia_especie.html", idespecie=idespecie)


@especie_blueprint.route("/image/<string:idespecie>")
def image(idespecie):
    return Imagem.especie_imagem(idespecie)


@especie_blueprint.route('/mostra')
def especies():
    data = Especie.find_all()
    fotos = Imagem.find_all()
    return render_template("especie/especies.html", data=data, fotos=fotos)


@especie_blueprint.route('/delete/<string:idespecie>')
@login_required
def delete_especie(idespecie):
    especie = Especie.find_by_id(idespecie)
    if especie is not None:
        Especie.delete(idespecie)

    return redirect(url_for(".especies"))


@especie_blueprint.route('/edit/<string:idespecie>', methods=['POST', 'GET'])
@login_required
def edit_especie(idespecie=None):
    especie = Especie.find_by_id(idespecie)
    if especie is not None:

        if request.method == 'POST':
            especie = request.form['especie']
            genero = request.form['genero']
            habitat = request.form['habitat']
            coordenadas = request.form['coordenadas']
            notas = request.form['notas']
            detalhes = request.form['detalhes']
            nomecomum = request.form['nomecomum']
            codigo = request.form['codigo']
            validacao = request.form['validacao']
            Especie.editar(idespecie, especie, genero, habitat, coordenadas, notas, detalhes, nomecomum, codigo,
                           validacao)
            return redirect(url_for(".especies"))

        return render_template("especie/edit_especie.html", especie=especie)

    return redirect(url_for(".especies"))


@especie_blueprint.route('/especie/completa/<string:idespecie>')
def especie_completa(idespecie):
    especie = Especie.find_by_id(idespecie)

    genero=''
    for (idespecie, especie, genero, habitat, coordenadas, notas, detalhes, nomecomum, codigo, validacao,
         datacriacao) in especie:
        genero = genero

    taxinomia = Especie.find_taxinomia(idespecie, genero)
    especie = Especie.find_by_id(idespecie)
    nome = QuemIdentificou.find_pessoa_especie(idespecie)
    encontrou = QuemEncontrou.find_pessoa_especie(idespecie)
    preservacao = PreservacaoEspecie.find_pessoa_especie(idespecie)
    fotos = Imagem.all_img_path(idespecie)

    return render_template('especie/especie_completa.html', data=especie,
                           identificacao=nome, encontrou=encontrou, preservacao=preservacao, id=idespecie, taxinomia=taxinomia, fotos=fotos)


@especie_blueprint.route('/imagems/<string:idespecie>')
def imagens(idespecie=None):
    especie = Especie.find_by_id(idespecie)
    genero = ''
    for (idespecie, especie, genero, habitat, coordenadas, notas, detalhes, nomecomum, codigo, validacao,
         datacriacao) in especie:
        genero = genero

    taxinomia = Especie.find_taxinomia(idespecie, genero)
    especie = Especie.find_by_id(idespecie)

    nome = QuemIdentificou.find_pessoa_especie(idespecie)
    encontrou = QuemEncontrou.find_pessoa_especie(idespecie)
    preservacao = PreservacaoEspecie.find_pessoa_especie(idespecie)
    fotos = Imagem.all_img_path(idespecie)
    return render_template('especie/imagens.html', fotos=fotos, id=idespecie, data=especie,
                           identificacao=nome, encontrou=encontrou, preservacao=preservacao,taxinomia=taxinomia)


@especie_blueprint.route('/pesquisa/<string:especie>', methods=['POST'])
def pesquisa_especie(especie=None):
    especies = Especie.find_pesquisa(especie)

    cabeca = txml.Element('especies')

    for (idespecie, especie, genero, habitat, coordenadas, notas, detalhes, nomecomum, codigo, validacao,
         datacriacao) in especies:
            element = txml.SubElement(cabeca, 'c_especie')
            elemento1 = txml.SubElement(element,'idespecie')
            elemento2 = txml.SubElement(element,'especie')
            elemento3 = txml.SubElement(element,'nomecomum')
            elemento4 = txml.SubElement(element,'habitat')

            elemento1.text = "{}".format(idespecie)
            elemento2.text = "{}".format(especie)
            elemento3.text = "{}".format(nomecomum)
            elemento4.text = "{}".format(habitat)

    my_xml = txml.tostring(cabeca)

    b = Response()
    b.set_data(my_xml)
    b.status = "200"
    b.get_json(force=False, silent=True, cache=True)
    b.mimetype = "application/xml"
    return b.get_data()
