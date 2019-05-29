from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired('Name required')])
    email = StringField('Email', validators=[DataRequired('Email address required'),Email('The email is not valid')])
    subject = StringField('Subject', validators=[DataRequired('Subject required')])
    message = TextAreaField('Message', validators=[DataRequired('Message required')])
    submit = SubmitField("Thank You!")