from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # Cria uma instância da classe Flask
app.secret_key = 'dragonballz'
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:admin@172.17.0.2/jogoteca'

db = SQLAlchemy(app)


class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Name {self.name}>'


class Usuarios(db.Model):
    nickname = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Name {self.name}>'


@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
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
    
    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash('Jogo já cadastrado!')
        return redirect(url_for('index'))
    
    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)

    db.session.add(novo_jogo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
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
