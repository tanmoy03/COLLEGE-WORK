import string
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField, DecimalField
from wtforms.validators import InputRequired, NumberRange

class ShiftForm(FlaskForm):
    plaintext = StringField("Plaintext:", validators=[InputRequired()])
    shift = IntegerField("Shift:", validators=[InputRequired(), NumberRange(1,25)])
    ciphertext = StringField("Ciphertext:")
    submit = SubmitField("Submit")

class ConversionForm(FlaskForm):
    before = RadioField("From:",
        choices = ["Farenheit", "Celsius", "Kelvin"], validators=[InputRequired()])
    tempbefore = DecimalField()
    after = RadioField("To:",
        choices = ["Farenheit", "Celsius", "Kelvin"], validators=[InputRequired()])
    tempafter = DecimalField()
    submit = SubmitField("Submit")
