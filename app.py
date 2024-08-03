from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from routes.auth import auth_bp
from routes.products import products_bp
from routes.stock import stock_bp
from routes.reports import reports_bp
from models import db
import os

app = Flask(__name__)

# Use a chave secreta gerada aqui
app.config['SECRET_KEY'] = 'your_secret_key'

# Configuração do banco de dados
if os.environ.get('FLASK_ENV') == 'development':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/stock_management_system'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:lucas2023@mysql/stock_management_system'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Configuração do LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# Função de carregamento de usuário para Flask-Login
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Tornar `current_user` disponível em todos os templates
@app.context_processor
def inject_user():
    return dict(current_user=current_user)

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
    app.run(host="0.0.0.0", port=5000, debug=True)
