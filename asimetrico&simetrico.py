import rsa
from cryptography.fernet import Fernet

#------------------Zona de encriptacion

#Se genera numero aleatorio para clave simetrica
clave = Fernet.generate_key()

#Se crean la clace asimetrica (publica y privada)
(pubkey,privkey)=rsa.newkeys(1024)

#Se genera el mensaje que sera encriptado
message = b'Mensaje encriptado'

#Se indica cual sera usado como Clava simetrico
f = Fernet(clave)
#Se encripta el mensaje
messcrypto = f.encrypt(message)
print("Mensaje de prueba para el ejercicio")
print(messcrypto)
#messDescrypt = f.decrypt(messcrypto)

#Se encripta la clave simetrica con la clave publica
pubcrypto = rsa.encrypt(clave,pubkey)
print("Clave simetrica encriptada")
print(pubcrypto)




#-----------------Zona de Desencriptacion-----------------------------

#Se descencripta la clave simetrica
privdecrypt = rsa.decrypt(pubcrypto,privkey)
print("Clave simetrica desencriptada")
print(privdecrypt)

#Se indica la clave con la que sera desencriptado el mensaje
S = Fernet(privdecrypt)
#Se desencripta el mensaje
messDescrypt = S.decrypt(messcrypto)
print("Mensaje desencriptado")
print(messDescrypt)
#print(decrypt.decode())
