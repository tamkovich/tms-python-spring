from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123")

cursor = conn.cursor()


def select_all():
    cursor.execute("SELECT * from products ORDER BY col_name")
    rows = cursor.fetchall()
    return rows


def select_something(product_id: int) -> list:
    cursor.execute("SELECT * from products WHERE id=(%s)", (iden,))
    rows = cursor.fetchall()
    return rows[0]


def delete_something(iden):
    cursor.execute("DELETE from products WHERE id=(%s)", (iden,))
    conn.commit()


def add_position(name, price, quantity, comment):
    cursor.execute('''INSERT INTO products
                   (col_name, col_price, col_quantity, col_comment)
                   VALUES (%s,%s,%s,%s)''', (name, price, quantity, comment))
    conn.commit()
    return "Позиция успешно добавлена"


# сделать потом красиво
def change_some_position(name, price, quantity, comment, iden):
    cursor.execute('''UPDATE products SET
                   col_name = %s WHERE id=%s''', (name, iden))
    cursor.execute('''UPDATE products SET
                   col_price = %s WHERE id=%s''', (price, iden))
    cursor.execute('''UPDATE products SET
                   col_quantity = %s WHERE id=%s''', (quantity, iden))
    cursor.execute('''UPDATE products SET
                   col_comment = %s WHERE id=%s''', (comment, iden))
    conn.commit()


@app.route('/')
def index():
    base_data = select_all()
    return render_template('list.html', base_data=base_data)


@app.route('/addposition/new', methods=['post', 'get'])
def add_new_position():
    if request.method == 'POST':
        name = request.form.get('name')
        price = float(request.form.get('price'))
        quantity = float(request.form.get('quantity'))
        comment = request.form.get('comment')
        add_position(name, price, quantity, comment)
        return redirect('/')  # это не работает
    return render_template('addposition.html')


@app.route('/stock/<iden>')
def show_position(iden):
    selected_position = select_something(iden)
    return render_template('showposition.html', selected_position=selected_position)


@app.route('/deleteposition/<iden>')
def delete_position(iden):
    delete_something(iden)
    return redirect('/')


@app.route('/changeposition/<iden>', methods=['post', 'get'])
def change_position(iden):
    position_info = select_something(iden)
    if request.method == 'POST':
        name = request.form.get('name')
        price = float(request.form.get('price'))
        quantity = float(request.form.get('quantity'))
        comment = request.form.get('comment')
        change_some_position(name, price, quantity, comment, iden)
    return render_template('changeposition.html', position_info=position_info)


if __name__ == '__main__':
    app.run()


# Написать сайт. Сайт предоставляет полный CRUD для работы с продуктами.
# Модель продукта состоит из id, name, price, amount, comment.
# На главной странице отображена краткая информация(id, name, price, amount)
# по всем продуктам. При нажатии на продукт происходит перенаправление на
# детализированную информацию по продукту. На детализированной странице продукта
# есть кнопки позволяющие отредактировать и удалить продукт.
