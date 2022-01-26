from flask_login import UserMixin

class User(UserMixin):
    """docstring fo User."""

    def __init__(self, id, username, password, distribuidor, grupo_trabajo):
        self.id = id
        self.username = username
        self.password = password
        self.distribuidor = distribuidor
        self.grupo_trabajo = grupo_trabajo
