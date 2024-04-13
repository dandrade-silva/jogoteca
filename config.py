import os

SECRET_KEY = 'dragonballz'

SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True

SQLALCHEMY_DATABASE_URI = \
    '{sgbd}://{usuario}:{senha}@{servidor}/{database}'.format(
        sgbd = 'mysql',
        usuario = 'root',
        senha = 'admin',
        servidor = '172.17.0.2',
        database = 'jogoteca'
    ) # 'mysql://root:admin@172.17.0.2/jogoteca'

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
