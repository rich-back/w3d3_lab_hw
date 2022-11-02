from flask import render_template
from app import app
from models.order_list import orders





@app.route('/orders')
def index():
    return render_template('index.html', title ='Home', orders=orders)

@app.route('/orders/1')
def order():
    return render_template('order.html', title ='Order', orders=orders)
