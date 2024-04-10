from flask import Flask, render_template # Importa a classe Flask


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack and Slash', 'PS2')
jogo3 = Jogo('Tomb Raider', 'Ação-Aventura', 'PS4')

lista_jogos = [jogo1, jogo2, jogo3]
    
app = Flask(__name__) # Cria uma instância da classe Flask


@app.route("/")
def home():
    return render_template('index.html', titulo="Jogos", jogos=lista_jogos)


# app.run() # Localhost
app.run(host='0.0.0.0', port=8080) # Pode ser acessado por pessoas conectadas nessa rede
