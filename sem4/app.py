from flask import Flask, render_template, request, url_for, redirect,session
from blueprint_basket.routes import blueprint_basket
from blueprint_auth.routes import blueprint_auth


app = Flask(__name__)

app.register_blueprint(blueprint_auth, url_prefix='/auth')
app.register_blueprint(blueprint_basket, url_prefix='/basket')
app.secret_key = 'PivoSecretKey'
role_mapping = [
        {'mpoint': '1', 'role': 'pivo'},
        {'mpoint': '2', 'role': 'pivovar'},
        {'mpoint': '1', 'role':  'andre'},
]
app.config['role_mapping'] = role_mapping


@app.route('/menu/', methods=['GET','POST'])
def main_menu():
    route_mapping = {
        '1': '/basket/basket/1',
        '2': '/basket/basket/2',
        '3': url_for('blueprint_auth.auth')}
 #   if 'user' in session:
 #       print('user_role = ', session['user'])
 #   else:
 #       print('Сессия пуста')
    point = request.args.get('point')
#    print('point =', point)
    if point is None:
        return render_template('main_menu.html',access='')
    elif point in route_mapping:
        return redirect(route_mapping[point])
    else:
        if 'user in session':
            session.pop('user')
        return 'До свиданья'



if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5001, debug = True)