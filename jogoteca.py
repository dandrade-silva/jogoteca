from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # TODO Configurar o DB

app = Flask(__name__)  # Cria uma instância da classe Flask

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)  # Pode ser acessado por pessoas conectadas nessa rede
