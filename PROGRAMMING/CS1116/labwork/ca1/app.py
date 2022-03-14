from flask import Flask, render_template, redirect, request, url_for, session, g
from database import get_db, close_db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
from forms import RegistrationForm, LoginForm
from functools import wraps

app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.before_request
def load_logging_in_user():
    g.user = session.get("user_id", None)

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return view(**kwargs)
    return wrapped_view

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vinyls")
def vinyls():
    db = get_db()
    vinyls = db.execute('''SELECT * FROM vinyls;''').fetchall()
    return render_template("vinyls.html", vinyls=vinyls)

@app.route("/vinyl/<int:vinyl_id>")
def vinyl(vinyl_id):
    db = get_db()
    vinyl = db.execute('''SELECT * FROM vinyls
                         WHERE vinyl_id = ?;''', (vinyl_id,)).fetchone()
    return render_template("vinyl.html", vinyl=vinyl)

@app.route("/cart")
@login_required
def cart():
    names = {}
    db = get_db()
    if "cart" not in session:
        session["cart"] = {}
    if session["cart"] == {}:
        return render_template("cart.html", cart=session["cart"], names=names)
    else:
        for vinyl_id in session["cart"]:
            vinyl = db.execute('''SELECT * FROM vinyls
                                WHERE vinyl_id = ?;''', (vinyl_id,)).fetchone()
            name = vinyl['name']
            names[vinyl_id] = name
        return render_template("cart.html", cart=session["cart"], names=names, vinyl=vinyl) 

@app.route("/add_to_cart/<int:vinyl_id>")
@login_required
def add_to_cart(vinyl_id):
    if "cart" not in session:
        session["cart"] = {}
    if vinyl_id not in session["cart"]:
        session["cart"][vinyl_id] = 0
    session["cart"][vinyl_id] = session["cart"][vinyl_id] + 1
    return redirect( url_for("cart") )

@app.route("/remove_from_cart/<int:vinyl_id>")
@login_required
def remove_from_cart(vinyl_id):
    # for some reason this function only works when removing an item only when 1 of the albums are in the cart. It doesn't work for multiple albums at once.
        if "cart" not in session:
            session["cart"] = {}
        if vinyl_id not in session["cart"]:
            session["cart"][vinyl_id] = 0
        if session["cart"][vinyl_id] > 0:
            session["cart"][vinyl_id] = session["cart"][vinyl_id] - 1 
        if session["cart"][vinyl_id] == 0: 
        # del function source: https://www.geeksforgeeks.org/python-del-to-delete-objects/#:~:text=The%20del%20keyword%20in%20python,dictionary%2C%20delete%20variables%2C%20etc.
            del session["cart"][vinyl_id]
        return redirect( url_for("cart") )

@app.route("/register", methods=["GET","POST"])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        password2 = form.password2.data
        db = get_db()
        matching_user = db.execute('''SELECT * FROM users
                            WHERE user_id=?;''', (user_id,)).fetchone()
        if matching_user is not None:
            form.user_id.errors.append("User id already taken!")
        else:
            db.execute('''INSERT INTO users (user_id, password)
                          VALUES (?, ?);''',
                          (user_id, generate_password_hash(password)))
            db.commit()
            return redirect( url_for("login"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        db = get_db()
        matching_user = db.execute('''SELECT * FROM users
                            WHERE user_id=?;''', (user_id,)).fetchone()
        if matching_user is None:
            form.user_id.errors.append("Unknown user id!")
        elif not check_password_hash(matching_user["password"], password):
            form.password.errors.append("Incorrect password!")
        else:
            session.clear()
            session["user_id"] = user_id
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("index")
            return redirect(next_page)
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    session.clear()
    return redirect( url_for("index") )