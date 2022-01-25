import gnupg
from ast import Try
import os

contenido = os.listdir('.\\ArchivoRecibidos\\')

print(contenido)

for x in contenido:
    try:
        #Ser recomienda ubicar el archivo y la claves en el mismo directorio para las pruebas.
        #Se indica la ruta donde se encuaentra las claves a utilizar
        gpg = gnupg.GPG(gnupghome = 'C:\\Users\\beto_\\Documents\\ServicioSocial\\ArchivoOpen')
        #Se importa clave publica para el descifrado
        key_data = open('secret-key-DFBF0E94.asc').read()
        import_result = gpg.import_keys(key_data)
        #print(import_result.results)

        #Se abre el archivo para cifrar el contenido, si se ubica en otra lado introducir ruta de la ubicacion
        with open('.\\ArchivoRecibidos\\'+x, 'rb') as f:
            #Se descifra el contenido y es introducido en un nuevo archivo
            status = gpg.decrypt_file(f, passphrase='1cG65xIyJj4Y5E98IRhscNIYP', output= x+'.txt')



        #Se importa clave Toka
        key_data = open('public-F40B9901.pgp').read()
        import_result = gpg.import_keys(key_data)
        #print(import_result.results)

        #Se abre el archivo para cifrar el contenido, si se ubica en otra lado introducir ruta de la ubicacion
        with open(x+'.txt', 'rb') as f:
            #Se cifra el contenido y es introducido en un nuevo archivo
            status = gpg.encrypt_file(f, recipients=import_result.fingerprints[0], armor=False, always_trust=True, output= '.\\ArchivoParaEnviar\\'+x)


            print ('ok: ', status.ok)
            print ('status: ', status.status)
            print ('stderr: ', status.stderr)

        os.remove('.\\'+x+'.txt')
    except:
        print('No hay archivo a cifrar.')








