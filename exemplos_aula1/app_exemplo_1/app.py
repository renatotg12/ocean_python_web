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

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/novo')
def novo():
    return render_template('novo.html')

if __name__ == '__main__':
    app.run()
