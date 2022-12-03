from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, DateField


class EmployeesForm(FlaskForm):
    email = EmailField('email')
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    phone = StringField('phone')
    address = StringField('address')
    birthday = DateField('birthday')
    submit = SubmitField('Save')