from functools import wraps
from flask import session,render_template,current_app


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' in session:
            return func(*args, **kwargs)
        else:
            return render_template('main_menu.html', access = 'Вам необходимо авторизоваться')
    return wrapper


def check_user(func):
    @wraps(func)
    def wrapper( mpoint ):
        if 'user' in session:
            role_mapping = current_app.config['role_mapping']
#        print('I am in check_role and mpoint =', mpoint)
            user_role = session.get('user')
 #       print('In session a=', a)
            for line in role_mapping:
#            print('point =', point['mpoint'], 'and role =', point['role'])
                if line['mpoint'] == mpoint and line['role'] == user_role:
                    return func(mpoint)
            return render_template('main_menu.html',access = 'У Вас нет прав на работу с этим пунктом меню')
        else:
            return render_template('main_menu.html',access = 'Вам необходимо авторизоваться')
    return wrapper


