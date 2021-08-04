from flask import Flask, render_template, session

from blueprint_basket.routes import blueprint_basket
from blueprint_auth.routes import blueprint_auth
from blueprint_query.routes import blueprint_query

app = Flask(__name__)

app.secret_key = 'PivoSecretKey'

app.register_blueprint(blueprint_auth, url_prefix='/auth')
app.register_blueprint(blueprint_basket, url_prefix='/basket')
app.register_blueprint(blueprint_query, url_prefix='/query')


@app.route('/', methods=['GET', 'POST'])
def main_menu():
    return render_template('index.html')


@app.route('/exit')
def exit_user():
    if 'user' in session:
        session.pop('user')
    return 'До свидания'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
