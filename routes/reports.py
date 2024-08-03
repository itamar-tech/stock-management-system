from flask import Blueprint, render_template
from models import Product, StockEntry, StockExit

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/inventory')
def inventory_report():
    products = Product.query.all()
    return render_template('inventory_report.html', products=products)

@reports_bp.route('/entries')
def entries_report():
    entries = StockEntry.query.all()
    return render_template('entries_report.html', entries=entries)

@reports_bp.route('/exits')
def exits_report():
    exits = StockExit.query.all()
    return render_template('exits_report.html', exits=exits)
