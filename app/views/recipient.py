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


@recipient_blueprint.route("/delete-recipient/<int:id>")
def delete_employye(id):
    employee = Recipient.query.get(id)
    employee.delete()
    flash("Employee was deleted", "success")
    return redirect(url_for("recipient.list"))


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


@recipient_blueprint.route("/change-employee/<int:id>", methods = ["GET", "POST"])
def change_employee(id):
    recipient: Recipient = Recipient.query.get(id)
    form = EmployeesForm(request.form)
    if form.validate_on_submit():
        recipient.email = form.email.data
        recipient.first_name = form.first_name.data,
        recipient.last_name = form.last_name.data,
        recipient.phone = form.phone.data,
        recipient.address = form.address.data,
        recipient.birthday = form.birthday.data,
        recipient.save()

        flash("You changed information of this employee", "success")
        return redirect(url_for('recipient.list'))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    elif request.method == "GET":
        form.email.data = recipient.email
        form.first_name.data = recipient.first_name
        form.last_name.data = recipient.last_name
        form.phone.data = recipient.phone
        form.address.data = recipient.address
        form.birthday.data = recipient.birthday
    return render_template("recipient/change_employee.html", form=form)