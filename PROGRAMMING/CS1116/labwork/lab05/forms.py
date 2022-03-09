from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import InputRequired

class GuessForm(FlaskForm):
    guess = DecimalField("Guess a number:", validators=[InputRequired()])
    submit = SubmitField("Submit")

