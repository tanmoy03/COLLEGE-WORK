from copy import error
from flask import Flask, render_template
from database import get_db, close_db
from forms import WinnersForm, MinWinnersForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

@app.route("/winners", methods=["GET", "POST"])
def winners():
    form = WinnersForm()
    winners = None
    if form.validate_on_submit():
        country = form.country.data
        db = get_db()
        winners = db.execute('''SELECT * FROM winners
                                    WHERE country = ?;''', (country,)).fetchall()
        if not winners:
            return render_template("winners_form.html", form=form, error="Error: Country not in Eurovision Winners database. Select another country.")
        else:
            return render_template("winners_form.html", 
                caption="Eurovision Winners", form=form, winners=winners)
    return render_template("winners_form.html", 
                caption="Eurovision Winners", form=form, winners=winners)

@app.route("/min_winners", methods=["GET","POST"])
def min_winners():
    form = MinWinnersForm()
    country = form.country.data
    points = form.points.data

    db = get_db()
    winners = db.execute('''SELECT * FROM winners''').fetchall()

    winners_by_country = db.execute('''SELECT * FROM winners
                            WHERE country = ?;''', (country,)).fetchall()
    winners_by_points = db.execute('''SELECT * FROM winners
                                      WHERE points>=?;''', (points,)).fetchall()
    winners_by_country_and_points = db.execute('''SELECT * FROM winners
                                                  WHERE country=?
                                                  AND points>=?;''', (country, points)).fetchall()
                                
    if winners_by_country and winners_by_points:
        return render_template("min_winners.html", form=form, winners_by_country_and_points=winners_by_country_and_points)
    elif winners_by_country:
        return render_template("min_winners.html", form=form, winners_by_country=winners_by_country)
    elif winners_by_points:
        return render_template("min_winners.html", form=form, winners_by_points=winners_by_points)


    return render_template("min_winners.html", form=form, winners=winners)
