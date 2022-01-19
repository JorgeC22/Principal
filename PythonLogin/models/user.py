from flask_login import UserMixin

class User(UserMixin):
    """docstring fo User."""

    def __init__(self, id, correo, passd, empresa):
        self.id = id
        self.correo = correo
        self.passd = passd
        self.empresa = empresa
