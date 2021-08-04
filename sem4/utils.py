from functools import wraps
from flask import session, render_template


def check_user(role):
    def wrapper_func(func):
        @wraps(func)
        def wrapper(point):
            if 'user' in session:
                if role == session.get('user'):
                    return func(point)
                return render_template('index.html', access='У Вас нет прав на работу с этим пунктом меню')
            else:
                return render_template('index.html', access='Вам необходимо авторизоваться')
        return wrapper
    return wrapper_func


