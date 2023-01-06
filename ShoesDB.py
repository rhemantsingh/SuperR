from flask import Flask, render_template, url_for, request, flash, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']="HEMANTisTHEbest"
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\heman\PycharmProjects\SuperR\DB\test.db'
db = SQLAlchemy(app)


class Logins(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Username = {self.username}"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    mrp = db.Column(db.Integer())
    color = db.Column(db.String(20))
    specification = db.Column(db.String(200))
    category = db.Column(db.String(20))
    subCategory = db.Column(db.String(20))

    def __repr__(self):
        return f"{self.name}{self.price}{self.link}{self.color}"

#db.init_app(app)


@app.route("/")
def home():
    products = Product.query.all()
    items = []
    for i in products:
        try:
            item = {
            "id": i.id,
            "name": i.name,
            "price": int(i.price),
            "specification": i.specification,
            "category": i.category,
            "subcategory": i.subCategory,
            "image": i.image,
            "mrp": int(i.mrp)
            }
            items.append(item)
        except:
            print(i.id)


    return render_template("home.html", items=items)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        name = request.form["name"]
        username = request.form["email"]
        password = request.form["pass"]
        try:
            find = db.session.execute(db.select(Logins).filter_by(username=username)).one()
            print(find)
        except:
            find = None
        if find is not None:
            print("Already Registered")
            flash("You are already Registered", "warning")
            return redirect(url_for("home"))
        else:
            print("New")
            user = Logins(name=name, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            flash("You are successfully Registered", "success")
            return redirect(url_for("home"))
    else:
        return render_template("Registration.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["email"]
        password = request.form["pass"]
        try:
            find = db.session.execute(db.select(Logins).filter_by(username=username,password=password)).one()
        except:
            find = None

        if find is not None:
            session["user"] = username
            return redirect(url_for("home"))
        else:
            flash("Entered data is incorrect", "danger")
            return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if session["user"]:
        session['user'] = None
        flash("You are successfully Logged Out", "success")
        return redirect(url_for("home"))
    else:
        flash("You are not logged in", "warning")
    return redirect(url_for("login"))


def checkLogin(fun):
    def first(*args, **kwargs):
        if session["user"]:
            fun(*args, **kwargs)
        else:
            return redirect(url_for("login"))

    return first()


@app.route("/item/<int:item_id>")
def item(item_id):
    if session["user"]:
        item = Product.query.filter_by(id=item_id).first()
        if item.mrp == "None":
            item.mrp = 0
        products = Product.query.all()
        recomend = []
        count = 0
        for i in products:
            if count > 5:
                break
            its = {
                "id": i.id,
                "name": i.name,
                "price": 0 if isinstance(i.price,str) else float(i.price),
                "specification": i.specification,
                "category": i.category,
                "subcategory": i.subCategory,
                "image": i.image,
                "mrp": 0 if isinstance(i.mrp,str) else float(i.mrp),
                "color": i.color
            }
            recomend.append(its)
            count = count+1
        return render_template("item.html", item=item, its=recomend)
    else:
        return redirect(url_for("login"))





@app.route("/A")
def A():
    if not session.get("user"):
        return redirect(url_for("login"))
    else:
        return render_template("A.html")


@app.route("/B")
def B():
    if not session.get("user"):
        return redirect(url_for("login"))
    else:
        return render_template("B.html")

