from app import create_app, db

app = create_app()

# Crear todas las tablas en la base de datos
with app.app_context():
    db.create_all()  # Esto asegura que las tablas definidas en los modelos sean creadas

if __name__ == '__main__':
    app.run(debug=True)
