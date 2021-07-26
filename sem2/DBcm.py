from pymysql.err import OperationalError
from pymysql import connect


class UseDatabase:
    def __init__(self, config: dict):
        self.config = config

    def __enter__(self):

        try:
            self.conn = connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor

        except OperationalError as err:
            if err.args[0] == 1045:
                print('Доступ запрещен. Проверьте логин и пароль')
            elif err.args[0] == 1049:
                print('Не удалось подключиться к базе данных, проверьте имя БД')
            else:
                print('error', err)
            return None

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:

        if exc_value is not None:
            if exc_value == 'Курсор не создан':
                print()
            else:
                print('!!!', exc_type,exc_value)
        else:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        return True

