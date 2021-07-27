import os
from flask import Blueprint
from flask import render_template, request, current_app,redirect
from db_model import work_with_db
from sql_provider import SQLProvider

blueprint_query = Blueprint('blueprint_query', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))
print('povider=',provider._scripts)

@blueprint_query.route('/student', methods=['POST', 'GET'])
def student_request():
    if request.method == 'GET':
        return render_template('input_form_request.html')
    elif request.method == 'POST':
        group_index = request.form.get('group_index')
#        print('Получен индекс', group_index)
        if group_index:
            _SQL = student_request(group_index)
            schema = ['name', 'birthday']
            print('_SQL=',_SQL)
            result = work_with_db(current_app.config['dbconfig'], _SQL, schema)
            return render_template('request_result.html',group_index =group_index, students=result)
        else:
            return "Wrong input for group_index"


def student_request(group_index):
    return provider.get('student', group_index=group_index)

