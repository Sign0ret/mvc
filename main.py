from app import create_app, db
from flask_login import LoginManager
from app.models import Usuario

app = create_app()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'routes.login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Create all tables in the database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)