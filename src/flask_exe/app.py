from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import redirect

app = Flask(__name__)
"""
    Подключаемся к базе даных в postgres
    предвариельно создав там базу test
"""
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://postgres:pass@localhost:5432/test"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

"""
    Создаем таблицу product и командой flask migrate and
    flask update создаем в нашей базе эту таблицу
"""
class ProductModel(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    comment = db.Column(db.String())

    def __init__(self, name, price, amount, comment):
        self.name = name
        self.price = price
        self.amount = amount
        self.comment = comment

    def __repr__(self):
        return f""

"""
    Далее код выполняет маршрутизацию среди страниц
    атакже логику по прасмотру добавению удалению изменению 
    записей в базе данныхх при помощи flask SQLAlchemy для 
    отображение инфомации на сайте использовал bootstrap для оформления 
    а также динамические страницы при помощи jinja
"""

@app.route("/product/set", methods=["POST", "GET"])
def handle_product_set():
    if request.method == "POST":
        if request.form:
            data2 = request.form
            new_product1 = ProductModel(
                name=data2["name"],
                price=int(data2["price"]),
                amount=int(data2["amount"]),
                comment=data2["comment"],
            )
            db.session.add(new_product1)
            db.session.commit()
            return redirect("/product")
        elif request.is_json:
            data = request.get_json()
            new_product = ProductModel(
                name=data["name"],
                price=data["price"],
                amount=data["amount"],
                comment=data["comment"],
            )
            db.session.add(new_product)
            db.session.commit()
            return redirect("/product")
        else:
            return {"error": "The request payload is not in format"}

    elif request.method == "GET":
        products = ProductModel.query.all()
        results = [
            {
                "name": product.name,
                "price": product.price,
                "amount": product.amount,
                "comment": product.comment,
            }
            for product in products
        ]

        return render_template(
            "datebase.html", post={"count": len(results), "product": results}
        )


@app.route("/product/change", methods=["POST", "GET"])
def handle_product_change():

    if request.method == "POST":
        product = ProductModel.query.get_or_404(int(request.form.get("id")))
        object_data = request.form
        product.name = object_data["name"]
        product.price = object_data["price"]
        product.amount = object_data["amount"]
        product.comment = object_data["comment"]
        db.session.add(product)
        db.session.commit()
        return redirect("/product")
    elif request.method == "GET":
        return render_template("change.html")


@app.route("/product/delete", methods=["POST", "GET"])
def handle_product_delete():

    if request.method == "POST":

        product = ProductModel.query.get_or_404(int(request.form.get("id")))
        db.session.delete(product)
        db.session.commit()
        return redirect("/product")

    elif request.method == "GET":
        return render_template("delete.html")


@app.route("/product")
def handle_product_get():
    products = ProductModel.query.order_by("id").all()
    results = [
        {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "amount": product.amount,
            "comment": product.comment,
        }
        for product in products
    ]

    return render_template(
        "create.html", post={"count": len(results), "product": results}
    )


@app.route("/")
def index():
    products = ProductModel.query.order_by("id").all()
    results = [
        {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "amount": product.amount,
            "comment": product.comment,
        }
        for product in products
    ]

    return render_template("index.html", post=results)


@app.route("/<id>", methods=["POST", "GET"])
def tets(id):
    product = ProductModel.query.get_or_404(id)
    if request.method == "POST":
        if request.form.get("delete"):
            db.session.delete(product)
            db.session.commit()
            return redirect("/")
        else:
            object_data = request.form
            product.name = object_data["name"]
            product.price = object_data["price"]
            product.amount = object_data["amount"]
            product.comment = object_data["comment"]
            db.session.add(product)
            db.session.commit()
            return redirect(f"/{id}")
    elif request.method == "GET":
        return render_template("chngdel.html", post=product)


if __name__ == "__main__":
    app.run()
