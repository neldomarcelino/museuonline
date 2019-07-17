# from flask import Flask, render_template, session
#
# from src.database.database import Database
# from src.models.Especie.especie import Especie
# from src.models.Reino.vista import reino_blueprint
# from src.models.Filo.vista import filo_blueprint
# from src.models.Classe.vista import classe_blueprint
# from src.models.Ordem.vista import ordem_blueprint
# from src.models.Familia.vista import familia_blueprint
# from src.models.Genero.vista import genero_blueprint
# from src.models.Especie.vista import especie_blueprint
# from src.models.Utilizador.vista import utilizador_blueprint
# from src.models.Imagem.imagem import Imagem
# from src.models.Utilizador.decorators import login_required_admin
# import src.config as config
#
#
# app = Flask(__name__)
# app.config.from_object(config)
# app.secret_key = "sdshfh923eew8/*+-1#$%^^!*"
#
# app.register_blueprint(reino_blueprint, url_prefix='/reinos')
# app.register_blueprint(filo_blueprint, url_prefix='/filos')
# app.register_blueprint(classe_blueprint, url_prefix='/classes')
# app.register_blueprint(ordem_blueprint, url_prefix='/ordems')
# app.register_blueprint(familia_blueprint, url_prefix='/familias')
# app.register_blueprint(genero_blueprint, url_prefix='/generos')
# app.register_blueprint(especie_blueprint, url_prefix='/especies')
# app.register_blueprint(utilizador_blueprint, url_prefix='/utilizadores')
#
#
# @app.before_first_request
# def inicializacaodb():
#     Database.connection()
#
#
# @app.route('/')
# def index():
#     fotos = Imagem.find_all()
#     especies = Especie.find_all()
#     return render_template('/home.html', fotos=fotos, especies=especies)
#
#
# @app.route('/home')
# def home():
#     fotos = Imagem.find_all()
#     especies = Especie.find_all()
#     return render_template('/home.html', fotos=fotos, especies=especies)
#
#
# @app.route('/admin')
# @login_required_admin
# def admin():
#     return render_template('admin/admin.html')
#
#
# if __name__== '__main__':
#     app.run(port=1786)
#
#
