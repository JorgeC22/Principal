#Se importa el modulo gnupg
import gnupg

#Ser recomienda ubicar el archivo y la claves en el mismo directorio para las pruebas.
#Se indica la ruta donde se encuaentra las claves a utilizar
gpg = gnupg.GPG(gnupghome = 'Ruta desde raiz hasta carpeta de claves')
#Se importa las claves
key_data = open('archivo/ruta a abrir y leer para importar claves').read()
import_result = gpg.import_keys(key_data)
#print(import_result.results)

#Se abre el archivo para cifrar el contenido, si se ubica en otra lado introducir ruta de la ubicacion
with open('archivo/ruta a abrir, leer y cifrar', 'rb') as f:
    #Se cifra el contenido y es introducido en un nuevo archivo
    status = gpg.encrypt_file(f, recipients='import_result.fingerprints[0]/correo', armor=False, always_trust=True, output='nombre y extension de archivo de salida')


    print ('ok: ', status.ok)
    print ('status: ', status.status)
    print ('stderr: ', status.stderr)
