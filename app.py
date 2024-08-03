
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth_bp
from routes.products import products_bp
from routes.stock import stock_bp
from routes.reports import reports_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(stock_bp, url_prefix='/stock')
app.register_blueprint(reports_bp, url_prefix='/reports')

if __name__ == '__main__':
    app.run(debug=True)
