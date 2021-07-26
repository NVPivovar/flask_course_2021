from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'


@app.route('/static')
def static_index():
    return render_template('static_index.html')


@app.route('/dynamic')
def dynamic_index():
    books = [{'author': 'Толстой', 'name': 'Анна Каренина', 'price': 23.4},
             {'author': 'Толстой', 'name': 'Война и мир', 'price': 48.8},
             {'author': 'Джек Лондон', 'name': 'Белый клык', 'price': 50.4}]
    book_tytle='Вот все наши книги'

    return render_template('dynamic_index.html', book_tytle=book_tytle, books=books )


# inherit html base
@app.route('/bitcoin')
def bitcoin_page():
    return render_template('bitcoin.html')



if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 5001, debug = True)