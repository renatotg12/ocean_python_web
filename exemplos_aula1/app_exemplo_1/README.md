# Tutorial de Exemplo em Python com Flask

Esta aplicação exibirá duas páginas diferentes, uma com uma mensagem de saudação e outra com uma mensagem personalizada.

**Passo 1: Preparação**

### 1. Verificar as dependências instaladas

Para saber se o "Flask" e o "Python-DotENV" estão instalados, no terminal, execute o comando:

```bach
pip freeze
```

### 2. Instalação do Flask 

Para executar essa aplicação, é necessário instalar o framework Flask.
Para isso, no terminal, execute o comando:

```bach
pip install flask
```

### 3. Instalação do Python DotENV

Para ativar o modo de depuração, instale a dependência "python-dotenv". Para isso, no terminal, execute o comando:
```bach
pip install python-dotenv
```

### 4. Configuração do arquivo `.flaskenv`

Crie o arquivo `.flaskenv` no diretório raiz da aplicação e adicione o código abaixo:

```bach
FLASK_APP=app.py
FLASK_DEBUG=1
```

**Passo 2: Criando a Estrutura do Projeto**

Primeiro, organize seu projeto em uma estrutura básica de pastas. Aqui, você pode criar uma pasta chamada `meu_app` para conter todos os arquivos relacionados ao seu aplicativo. Dentro dela, crie um arquivo chamado `app.py` para o código Flask.

```
meu_app/
    app.py
    templates/
        hello.html
        novo.html
```

**Passo 3: Criando os Templates HTML**

Agora, crie dois arquivos HTML dentro da pasta `templates` que serão renderizados pelo Flask.

- `hello.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Página de Saudação</title>
</head>
<body>
    <h1>Olá, Renato!</h1>
</body>
</html>
```

- `novo.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Nova Página</title>
</head>
<body>
    <h1>Bem-vindo à Nova Página!</h1>
</body>
</html>
```

**Passo 4: Criando a Aplicação Flask**

Agora, você pode usar o Flask para criar uma aplicação web simples que renderiza esses templates HTML. Abra o arquivo `app.py` e insira o seguinte código:

```python
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
```

**Passo 5: Executando a Aplicação**

Agora que tudo está configurado, você pode executar sua aplicação Flask. Abra o terminal na pasta raiz do seu projeto (`meu_app`) e execute o seguinte comando:

```
flask run
```

Você verá uma saída indicando que o servidor Flask está em execução.

**Passo 6: Acessando a Aplicação**

Abra um navegador e acesse `http://localhost:5000/` para ver a primeira página com a saudação "Olá, Renato!" e acesse `http://localhost:5000/novo` para ver a segunda página com a mensagem "Bem-vindo à Nova Página!".

Agora você criou uma aplicação web simples com Flask que exibe duas páginas HTML diferentes. Este é apenas um exemplo básico para começar, e você pode expandir sua aplicação e melhorá-la de acordo com suas necessidades.