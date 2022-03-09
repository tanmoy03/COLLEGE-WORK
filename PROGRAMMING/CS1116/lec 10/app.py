from flask import Flask, render_template, request, make_response
from forms import VoteForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

@app.route("/vote", methods=["GET", "POST"])
def vote():
    form = VoteForm()
    if request.cookies.get("voted") == "yes":
        return render_template("feedback.html", 
            message= "Sorry, you already voted")
    if form.validate_on_submit():
        vote = form.vote.data
        # update database with the new vote
        # db = get_db()
        # db.execute("UPDATE...")
        response = make_response(render_template("feedback.html", 
            message = "Thanks for your vote!"))
        response.set_cookie("voted","yes")
        return response
    return render_template("vote_form.html", form=form)