import gnupg

#Ser recomienda ubicar el archivo y la claves en el mismo directorio para las pruebas.
gpg = gnupg.GPG(gnupghome = 'ruta completa donde se ubican las claves')
key_data = open('nombre_archivo que contiene la claves a importar').read()
import_result = gpg.import_keys(key_data)
print(import_result.results)

with open('nombre/ruta del archivo a abrir', 'rb') as f:
    status = gpg.encrypt_file(f, recipients= '', output='file.txt.gpg')


print ('ok: ', status.ok)
print ('status: ', status.status)
print ('stderr: ', status.stderr)
