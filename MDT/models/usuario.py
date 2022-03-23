import imp
from flask_login import UserMixin
import bcrypt
from conexion import *

class usuario(UserMixin):

    def __init__(self, id_usuario, nombre_usuario, contraseña) -> None:
        self.id = id_usuario
        self.username = nombre_usuario
        self.password = contraseña