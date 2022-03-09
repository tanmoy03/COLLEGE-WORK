from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.datetime import DateField
from wtforms.validators import InputRequired, EqualTo

class BandForm(FlaskForm):
    band = StringField("Band:", validators=[InputRequired()])
    submit = SubmitField("Submit")

class GigForm(FlaskForm):
    band = StringField("Band:", validators=[InputRequired()])
    gig_date = DateField("Gig date:", validators=[InputRequired()])
    submit = SubmitField("Submit")

class RegistrationForm(FlaskForm):
    user_id = StringField("User id:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    password2 = PasswordField("Confirm password:", 
        validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Submit")