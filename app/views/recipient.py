from flask import Blueprint, redirect, url_for, flash, render_template, request
from flask_login import login_required

from app.models import Recipient
from app.forms import EmployeesForm

recipient_blueprint = Blueprint("recipient", __name__)


@recipient_blueprint.route("/recipients", methods=["GET", "POST"])
@login_required
def list():
    recipients = Recipient.query.all()
    return render_template("recipient/list.html", recipients=recipients)


@recipient_blueprint.route("/add-employee", methods = ["GET", "POST"])
def add_employee():
    form = EmployeesForm(request.form)
    if form.validate_on_submit():
        empoloyee = Recipient(
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone=form.phone.data,
            address=form.address.data,
            birthday=form.birthday.data,
        )
        empoloyee.save()
        flash("You added a new employee", "success")
        return redirect(url_for("recipient.list"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    return render_template("recipient/add_employee.html", form = form)