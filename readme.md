## Sistema de Citas de Hospital MVC utilizando FLASK.
- Adolfo Hernández Signoret
    - Modelo
    - Clases Dao
    - Controlador
- Bryan Ithan Landín Lara
    - Rutas
    - Vistas

## Modelo
- administrador.py & administrador_dao.py
- cita.py & cita_dao.py
- enfermera.py & enfermera_dao.py
- medico.py & medico_dao.py
- paciente.py & paciente_dao.py
- usuario.py & usuario_dao.py

## Vista
- citas.html
- login.html
- register.html
- usuarios.html

## Controlador
- cita_controller.py
- usuario_controller.py

## Conectores entre las partes
- Modelo-Controlador = Clase DAO
- Controlador-Vista = routes.py

## Base de datos
- main.py
- instance/database.db (se crea solo al correrlo)
- migrations/

## Comandos para instalar
1. Activar el virtual environment
```
python3 -m venv env
```
```
source env/bin/activate
```
2. Instalar las dependencias
```
pip install -r requirements.txt
```
3. Ejecutar el programa
```
python3 main.py
```
4. Probarlo en el puerto http://127.0.0.1:5000/login
5. Entrar con la cuenta de administrador creada default: Admin, admin1234.