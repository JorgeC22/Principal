from cryptography.fernet import Fernet

clave = Fernet.generate_key()

print(clave)
print("######################################################")

f = Fernet(clave)


message = b'Mensaje encriptado'

messcrypto = f.encrypt(message)

print(messcrypto)

messDescrypt = f.decrypt(messcrypto)

print(messDescrypt)
