from flask import Flask, url_for, request, render_template, redirect
from blueprint_query.blueprint_query import blueprint_query

app = Flask(__name__)


app.register_blueprint(blueprint_query,url_prefix='/zaproses')

main_menu = [{"name": "Запросы", "url": "?point=1"},
 {"name": "Отчеты", "url": "?point=2"},
 {"name":  "Что-то еще",  "url":  "?point=3"},
 {"name": "Выход",  "url": "?point=exit"}]

app.config['dbconfig'] = {"host" : "127.0.0.1",
                "user" : "root",
                "password" : "root",
                "database" : "Decanat"}



@app.route('/menu/')
def menu():

    route_mapping = {
        '1': url_for('blueprint_query.student_request'),
        '2': url_for('menu'),
        '3': url_for('menu'),
    }
    point = request.args.get('point')
    print("point=", point)

    if point is None:
        return render_template('main_menu.html', menu=main_menu)

    elif point in route_mapping:
        return redirect(route_mapping[point])

    else:
        return "До свидания, заходите к нам еще!!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)