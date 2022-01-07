import Crypto
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

#Se crea numero aleatorio.
random_generator = Crypto.Random.new().read

private_key = RSA.generate(1024)
public_key = private_key.publickey()

print("#######################################################################")
print(private_key)
print(public_key)

private_key = private_key.exportKey(format='DER')
public_key = public_key.exportKey(format='DER')

private_key = binascii.hexlify(private_key).decode('utf8')
public_key = binascii.hexlify(public_key).decode('utf8')

print("#######################################################################")
print(private_key)
print(public_key)

#proceso inverso

private_key = RSA.importKey(binascii.unhexlify(private_key))
public_key = RSA.importKey(binascii.unhexlify(public_key))

message = "Hola mundo desde un string en texto plano!"
message = message.encode()

print("#######################################################################")

cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(message)

print(encrypted_message)

cipher = PKCS1_OAEP.new(private_key)
message = cipher.decrypt(encrypted_message)

print(message)
