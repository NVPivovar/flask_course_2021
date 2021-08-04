from flask import Blueprint, session, redirect


blueprint_auth = Blueprint('blueprint_auth', __name__)


@blueprint_auth.route('/', methods=['GET', 'POST'])
def auth():
    session['user'] = 'typical'
    return redirect('/')
