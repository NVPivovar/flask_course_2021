import os
from flask import Flask, request, render_template, redirect
from db_work import work_with_db

app = Flask(__name__)

dbconfig = {'host': '127.0.0.1','user': 'root','password': 'root','database': 'Decanat'}

@app.route('/')
@app.route('/<param>')
def index(param=None):
    if param is None:
        return 'Hello world'
    else:
        return f'Hello {param}'


@app.route('/users/<int:user_id>')
def user_page(user_id: int):

    users = [
        {'id': 1, 'name': 'Nick', 'email': 'nick@google.com'},
        {'id': 2, 'name': 'Mike', 'email': 'mike@google.com'},
        {'id': 3, 'name': 'John', 'email': 'john@google.com'},
    ]

    user = None
    for _user in users:
        if _user['id'] == user_id:
            user = _user
            break

    if user is None:
        return 'Not found'
    return f"User profile:\nname: {user['name']}\nemail: {user['email']}"

@app.route('/sum')  # Доп. задание - калькулятор на args
def page_with_args():
    x = float(request.args.get('x', 1))
    y = float(request.args.get('y', 3))
    return f'Result: {x + y}'

@app.route('/user-form')
def user_input_page_1():
    return render_template('input_form_redirect.html')


@app.route('/user-form-next', methods=['POST'])
def user_input_page_2():
    login = request.form.get('login', '')
    password = request.form.get('password', '')
    if login and password:
        return {'login': login, 'password': password}
    else:
        return 'Wrong input'


@app.route('/user-form-all', methods=['GET', 'POST'])  # Доп. - получить данные пользователя и вернуть страничку с его профилем
def user_input():
    if request.method == 'GET':
        return render_template('input_form_self.html')
    elif request.method == 'POST':
        login = request.form.get('login', None)
        password = request.form.get('password', None)
        if login and password:
            return redirect('/')
        else:
            return 'Wrong input'


@app.route('/user-request', methods=['GET', 'POST'])
def user_request():
    if request.method == 'GET':
        return render_template('input_form_request.html')
    elif request.method == 'POST':
        group_index = request.form.get('group_index')
        if group_index:
            _SQL = f"""select s_name,birthday from student join s_group using(g_id)
                        where g_index='{group_index}'"""
            schema = ['name', 'birthday']
            result = work_with_db(dbconfig, _SQL, schema)
        else:
            return "Wrong input for group_index"
        if result:
            return render_template('request_result.html', group_index=group_index, students=result)


@app.route('/upload-file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('input_file.html')
    elif request.method == 'POST':
        file = request.files.get('file')
        if file.filename:
            file.save(os.path.join('static/images/', file.filename))
            return render_template('image_page.html', url=os.path.join('/static/images/', file.filename))
        else:
            return render_template('input_file.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)

