from classes import SQLiteDataBase
from flask import Flask
from flask import render_template
from flask import request
import os
from shutil import copy

app = Flask(__name__)


@app.route('/')
def index():
    global db, table
    return render_template('index.html', all_items=db.get_all_items(table))


@app.route('/edit/<int:item_id>', methods=['POST', 'GET'])
def edit(item_id: int):
    global db, table

    if request.method == 'POST':
        if request.form.get('delete'):
            db.delete_item_by_id(table, item_id)
        else:
            name = request.form.get('name')
            price = request.form.get('price')
            count = request.form.get('count')
            comment = request.form.get('comment')
            db.update_item_by_id(table, item_id,
                                 name=name, price=price, count=count, comment=comment)

        return render_template('index.html', all_items=db.get_all_items(table))
    return render_template('edit.html', item=db.get_item_by_id(table, item_id=item_id))


@app.route('/add/', methods=['POST', 'GET'])
def add():
    global db, table
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        count = request.form.get('count')
        comment = request.form.get('comment')
        db.add_item(table, name=name, price=price, count=count, comment=comment)
        return render_template('index.html', all_items=db.get_all_items(table))
    return render_template('add.html')


@app.route('/restore/')
def restore():
    global db, database_path
    database_origin = os.path.join(os.getcwd(), 'products_origin.db')
    copy(database_origin, database_path)
    return render_template('index.html', all_items=db.get_all_items(table))


database_path = os.path.join(os.getcwd(), 'products.db')
db = SQLiteDataBase(database_path)
table = 'products'

if __name__ == '__main__':
    app.run()
