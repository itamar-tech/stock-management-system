from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, StockEntry, StockExit, Product

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/entry', methods=['GET', 'POST'])
def stock_entry():
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        new_entry = StockEntry(product_id=product_id, quantity=quantity)
        product = Product.query.get(product_id)
        product.quantity += int(quantity)
        db.session.add(new_entry)
        db.session.commit()
        flash('Entrada de estoque registrada com sucesso!')
        return redirect(url_for('stock.stock_entry'))

    products = Product.query.all()
    return render_template('stock_entry.html', products=products)

@stock_bp.route('/exit', methods=['GET', 'POST'])
def stock_exit():
    if request.method == ['POST']:
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        new_exit = StockExit(product_id=product_id, quantity=quantity)
        product = Product.query.get(product_id)
        if product.quantity >= int(quantity):
            product.quantity -= int(quantity)
            db.session.add(new_exit)
            db.session.commit()
            flash('Saída de estoque registrada com sucesso!')
        else:
            flash('Quantidade em estoque insuficiente!')
        return redirect(url_for('stock.stock_exit'))

    products = Product.query.all()
    return render_template('stock_exit.html', products=products)
