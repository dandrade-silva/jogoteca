from flask import Flask, render_template, request, redirect, session, flash, url_for


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack and Slash', 'PS2')
jogo3 = Jogo('Tomb Raider', 'Ação-Aventura', 'PS4')

lista = [jogo1, jogo2, jogo3]


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Danilo", "dandrade", "123")
usuario2 = Usuario("Luane", "luanealmeida", "456")

usuarios = { usuario1.nickname : usuario1,
             usuario2.nickname : usuario2 }


app = Flask(__name__) # Cria uma instância da classe Flask
app.secret_key = 'dragonballz'
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True


@app.route('/')
def index():
    return render_template('index.html', titulo='Jogos', jogos=lista)


@app.route('/cadastro')
def cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', next=url_for('cadastro')))
    return render_template('cadastro.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)

    lista.append(jogo)
    
    return redirect(url_for('index'))


@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['next']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if session['usuario_logado'] == None:
        flash('Nenhum usuário está logado')
        return redirect(url_for('index'))
    else:
        session['usuario_logado'] = None
        flash('Logout efetuado com sucesso')
        return redirect(url_for('index'))

# app.run() # Localhost
app.run(debug=True) # Pode ser acessado por pessoas conectadas nessa rede
