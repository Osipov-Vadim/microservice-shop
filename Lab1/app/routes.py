from flask import render_template, flash, redirect, url_for, request, session
from app import app, db
from app.models import *
from app.forms import *

@app.route('/')
@app.route('/index')
def index():
    return "<h1>This is payment service</h1>"

@app.route('/api/orders/<order_id>/payment',methods=['GET', 'POST'])
def perform_payment(order_id):
    form = PaymentForm()
    order = Order.query.filter_by(id = order_id).first()
    if form.validate_on_submit():
        if form.status.data == 'AUTHORIZED':
            order.status = "PAID"
            db.session.commit()
            return "<h1>Order " + str(order_id) + " paid completed!</h1>"
            # return redirect(url_for("index"))
    return render_template("perform_payment.html", form = form)


@app.route('/api/orders/<order_id_>/status/<status>',methods=['GET', 'POST'])
def change_order_status(order_id_, status):
    order = Order.query.filter_by(id = order_id_).first()
    order.status = status
    db.session.commit()
    return "<h2> Status of " + str(order_id_) + " has been changed to " + status + "</h2>"
