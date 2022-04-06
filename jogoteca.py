from flask import Flask, render_template, request


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('god of war', 'Rack and slash', 'ps2')
jogo2 = Jogo('Horizon Zero Dawn', 'adventure', 'ps4')
lista = [jogo1, jogo2]


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos=lista)


@app.route('/novoJogo')
def novo():
    return render_template('novo_jogo.html', titulo = 'Cadastrar Novo Jogo' )


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo = 'Jogos', jogos=lista)


app.run(debug=True)
