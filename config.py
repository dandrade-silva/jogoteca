import os

SECRET_KEY = 'dragonballz'

SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True

SQLALCHEMY_DATABASE_URI = \
    '{sgbd}://{usuario}:{senha}@{servidor}/{database}'.format(
        sgbd='mysql+mysqlconnector',
        usuario='root',
        senha='admin',
        servidor='localhost',
        database='jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
