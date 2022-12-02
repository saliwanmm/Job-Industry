from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField


class EmployeesForm(FlaskForm):
    email = EmailField('email')
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    phone = StringField('phone')
    address = StringField('address')
    birthday = StringField('birthday')
    submit = SubmitField('Save')