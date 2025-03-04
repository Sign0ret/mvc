from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Asegúrate de importar Migrate

# Inicializar SQLAlchemy y Flask-Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar rutas
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app

