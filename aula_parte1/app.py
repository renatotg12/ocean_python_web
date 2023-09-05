# Para executar essa aplicação, é necessário instalar o framework Flask.
# Para isso, no terminal, execute o comando:
# pip install flask

# Para ativar o modo de depuração, instale a dependência python-dotenv.
# pip install python-dotenv

# Crie o arquivo .flaskenv e adicione o código abaixo:
# FLASK_APP=app.py
# FLASK_DEBUG=1

# Para saber se o Flask está instalado, no terminal, execute o comando:
# pip freeze

# Importa o framework Flask
from flask import Flask

# Cria uma intancia da class Flask
app = Flask("meu app")

# Defini uma rota
@app.route('/')
def hello():
    return "Hello Renato"

@app.route('/novo')
def novo():
    return "Nova página"