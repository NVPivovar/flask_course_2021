from flask import Blueprint
from flask import render_template, request, current_app,redirect
from db_model import work_with_db

blueprint_query = Blueprint('blueprint_query', __name__, template_folder='templates')

@blueprint_query.route('/student', methods=['POST', 'GET'])
def student_request():
    if request.method == 'GET':
        return render_template('input_form_request.html')
    elif request.method == 'POST':
        group_index = request.form.get('group_index')
        print('Получен индекс', group_index)
        if group_index:
            _SQL = f"""select s_name,birthday from student join s_group using(g_id)
                        where g_index='{group_index}'"""
            schema = ['name', 'birthday']
            print('_SQL=',_SQL)
            result = work_with_db(current_app.config['dbconfig'], _SQL, schema)
            print('!!!!',result)
            return render_template('request_result.html',group_index =group_index, students=result)
        else:
            return "Wrong input for group_index"

def

