from flask import Blueprint,session,redirect


blueprint_auth = Blueprint('blueprint_auth', __name__, template_folder='templates')

@blueprint_auth.route('/auth', methods = ['GET','POST'])
def auth():
    login = 'Pivovar'
    role = 'pivo'
    session['user'] = role
    print('Сесия сформирована')
    return redirect('/menu?')
