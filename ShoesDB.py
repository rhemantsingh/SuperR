from flask import Flask,render_template,url_for, request, flash,redirect,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']="HEMANTisTHEbest"
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\hemant.singh.rawat\PycharmProjects\Selenium_EXT\DB\test.db'
db = SQLAlchemy(app)

class Logins(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Username = {self.username}"

class Laptop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

#db.init_app(app)

@app.route("/")
def Home():
    return render_template("Welcome.html")

@app.route("/register", methods=["GET","POST"])
def Register():
    if request.method == 'POST':
        name = request.form["name"]
        username = request.form["email"]
        password = request.form["pass"]
        try:
            find = db.session.execute(db.select(Logins).filter_by(username=username)).one()
            print(find)
        except:
            find=None
        if find != None:
            print("Already Registered")
            flash("You are already Registered")
            return redirect(url_for("Home"))
        else:
            print("New")
            user = Logins(name=name, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            flash("You are successfully Registered")
            return redirect(url_for("Home"))

    else:
        return render_template("Registration.html")


@app.route("/login", methods=["GET","POST"])
def Login():
    if request.method == "GET":
        return render_template("Login.html")
    else:
        username = request.form["email"]
        password = request.form["pass"]
        try:
            find = db.session.execute(db.select(Logins).filter_by(username=username,password=password)).one()
        except:
            find = None

        if find!=None:
            session["user"] = username
            return redirect(url_for("A"))
        else:
            flash("Entered data is incorrect")
            return redirect(url_for("Login"))

@app.route("/A")
def A():
    if not session.get("user"):
        return redirect(url_for("Login"))
    else:
        return render_template("A.html")

@app.route("/B")
def B():
    if not session.get("user"):
        return redirect(url_for("Login"))
    else:
        return render_template("B.html")

@app.route("/logout")
def Logout():
    session['user']=None
    flash("You are successfully Logged Out")
    return redirect(url_for("Home"))


@app.route("/name")
def Name():
    S = Logins.query.all()
    return f"the Database data {S}"