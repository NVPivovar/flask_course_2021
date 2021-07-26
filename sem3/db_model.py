from DBcm import UseDatabase


def work_with_db(dbconfig: dict, _SQL: str, schema: list):
    with UseDatabase(dbconfig) as cursor:
        print('cursor =',cursor)
        if cursor is None:
            raise ValueError('Курсор не создан')

        cursor.execute(_SQL)
#        column_numb = len(cursor.description)
#        print('column_numb = ', column_numb)
        result = []

        for student_tuple in cursor.fetchall():
            student_dict = dict(zip(schema, student_tuple))
            result.append(student_dict)
#    print(result)
    return result

