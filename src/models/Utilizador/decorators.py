from functools import wraps
from flask import g, request, redirect, url_for, session
from src.config import ADMINS


def login_required_user(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('utilizador.login_user', next=request.path))
        return f(*args, **kwargs)
    return decorated_function


def login_required_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('utilizador.login_user', next=request.path))

        if session['email'] not in ADMINS:
            print("{}kjjjjjjjjjjjjjjjjjjjjjj".format(session['email']))
            return redirect(url_for('utilizador.login_user', message="E necessatio permissao de administrador"))

        return f(*args, **kwargs)
    return decorated_function
