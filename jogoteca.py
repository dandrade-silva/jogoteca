from flask import Flask, render_template, request, redirect, session, flash


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack and Slash', 'PS2')
jogo3 = Jogo('Tomb Raider', 'Ação-Aventura', 'PS4')

lista = [jogo1, jogo2, jogo3]
    
app = Flask(__name__) # Cria uma instância da classe Flask
app.secret_key = 'dragonballz'
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True


@app.route('/')
def home():
    return render_template('index.html', titulo='Jogos', jogos=lista)


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo='Jogos')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)

    lista.append(jogo)
    
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['senha'] == 'goku':
        session['usuario_logado'] = request.form['usuario']
        flash(f'{session['usuario_logado']} logado com sucesso.')
        return redirect('/')
    else:
        flash('Dados incorretos! Tente novamente.')
        return redirect('/login')

@app.route('/logout')
def logout():
    if session['usuario_logado'] == None:
        flash('Nenhum usuário está logado')
        return redirect('/')
    else:
        session['usuario_logado'] = None
        flash('Logout efetuado com sucesso')
        return redirect('/')

# app.run() # Localhost
app.run(debug=True) # Pode ser acessado por pessoas conectadas nessa rede
