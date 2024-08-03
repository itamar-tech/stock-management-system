from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def list_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@products_bp.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        code = request.form['code']
        quantity = request.form['quantity']
        cost_price = request.form['cost_price']
        sale_price = request.form['sale_price']
        expiration_date = request.form['expiration_date']
        
        new_product = Product(
            name=name, 
            code=code, 
            quantity=quantity, 
            cost_price=cost_price, 
            sale_price=sale_price, 
            expiration_date=expiration_date
        )
        
        db.session.add(new_product)
        db.session.commit()
        flash('Produto adicionado com sucesso!')
        return redirect(url_for('products.list_products'))
    
    return render_template('add_product.html')
