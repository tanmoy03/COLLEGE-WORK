from flask_wtf import FlaskForm
from wtforms import BooleanField, RadioField, SubmitField
from wtforms.validators import InputRequired

class AliveForm(FlaskForm):
    alive = BooleanField("Check the box if you think Elvis is still alive:")
    submit = SubmitField("Submit")

class ToppingForm(FlaskForm):
    topping = RadioField("Which topping do you think Elvis prefers?",
        choices = ["anchovies", "chocolate", "morphine", "finger nails"],
        validators=[InputRequired()])
    submit = SubmitField("Submit")