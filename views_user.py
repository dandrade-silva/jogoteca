from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash


@app.route('/login')
def login():
    next = request.args.get('next')
    form = FormularioUsuario()
    return render_template('login.html', next=next, form=form)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
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

# TODO criar formulário de cadastro para novos usuários
"""
Exemplo de rota
@app.route('/novo_usuario', methods=['POST',])
def novo_usuario():
    form = FormUser(request.form)
    nome = form.nome.data
    idade = form.idade.data
    senha = generate_password_hash(form.senha.data).decode('utf-8')

    new_user = Usuarios(nome=nome, idade=idade, senha=senha)
    db.session.add(new_user)
    db.session.commit()
"""