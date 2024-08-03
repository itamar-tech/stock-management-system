from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.auth import auth_bp
from routes.products import products_bp
from routes.stock import stock_bp
from routes.reports import reports_bp
from models import db

app = Flask(__name__)

# Use a chave secreta gerada aqui
app.config['SECRET_KEY'] = '5cce427c00da41941d7c0b58948494bf66b8a6dcdf02440a'

# Atualize a string de conexão para omitir a senha
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/stock_management_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Registrando as blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(stock_bp, url_prefix='/stock')
app.register_blueprint(reports_bp, url_prefix='/reports')

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
