from dataclasses import field
from click import command
from flask import session
import paramiko
import os
import gnupg
import scp

#========== Extraccion de archivo del servidor.
def extracccion():
    print('Buscando Archivos........................')
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.load_system_host_keys()

    key_file = paramiko.RSAKey.from_private_key_file('C:/Users/beto_/Documents/ServicioSocial/SSHconection/id_rsa','holamundo')

    session.connect(
        hostname='192.168.1.158',
        username='root',
        pkey=key_file,
        allow_agent=False,
        look_for_keys=False
    )

    sftp_client = session.open_sftp()

    #sftp_client.put('C:/Users/beto_/Documents/ServicioSocial/Cifradotoka/archivos_26_01_2022.zip','/home/ec2-user/archivos_26_01_2022.zip')

    list = sftp_client.listdir('/root/archivos_26_01_2022')
    list2 = []
    #print(list)
    if list:
        print('Existe una lista de archivos.')
        for x in list:
            cadena = x.find('.PGP')
            if cadena != -1:
                list2.append(x)

    
    if list2:
        print('Existe archivos a cifrar.')
        print('Extrallendo Archivos......................')
        for x in list2:
            sftp_client.get('/root/archivos_26_01_2022/'+x,'./ArchivoRecibidos/'+x)
        print('Archivos Extraidos.')
        extraccion = True
    else:
        print('No Existen archivos a cifrar.')
        extraccion = False
    
    sftp_client.close()
    return extraccion

#========== Cifrado de los archivos extraidos.
def cifradoPGP():
    print('Cifrando archivos............................')
    ruta = 'C:/Users/beto_/Documents/ServicioSocial/ArchivoOpen'
    contenido = os.listdir(ruta+'/ArchivoRecibidos/')

    #print(contenido)

    if contenido:
        try:
            for x in contenido:
                file = x.replace('.PGP','.gpg')
                #Ser recomienda ubicar el archivo y la claves en el mismo directorio para las pruebas.
                #Se indica la ruta donde se encuaentra las claves a utilizar
                gpg = gnupg.GPG(gnupghome = ruta)
                #Se importa clave publica para el descifrado
                key_data = open(ruta+'/secret-key-DFBF0E94.asc').read()
                import_result = gpg.import_keys(key_data)
                #print(import_result.results)

                #Se abre el archivo para cifrar el contenido, si se ubica en otra lado introducir ruta de la ubicacion
                with open(ruta+'/ArchivoRecibidos/'+x, 'rb') as f:
                    #Se descifra el contenido y es introducido en un nuevo archivo
                    status = gpg.decrypt_file(f, passphrase='1cG65xIyJj4Y5E98IRhscNIYP', output= ruta+'/'+x+'.txt')

                

                #Se importa clave Toka
                key_data = open(ruta+'/public-F40B9901.pgp').read()
                import_result = gpg.import_keys(key_data)
                #print(import_result.results)

                #Se abre el archivo para cifrar el contenido, si se ubica en otra lado introducir ruta de la ubicacion
                with open(ruta+'/'+x+'.txt', 'rb') as f:
                    #Se cifra el contenido y es introducido en un nuevo archivo
                    status = gpg.encrypt_file(f, recipients=import_result.fingerprints[0], armor=False, always_trust=True, output= ruta+'/ArchivoParaEnviar/'+file)


                    #print ('ok: ', status.ok)
                    #print ('status: ', status.status)
                    #print ('stderr: ', status.stderr)

                os.remove(ruta+'/ArchivoRecibidos/'+x)
                os.remove(ruta+'/'+x+'.txt')
            print('Archivos Cifrados correctamente.')
            cifrado = True
        except:
            print('Error: No se pueden cifrar los archivos.')
            cifrado = False
    else:
        print('No existen archivos a cifrar.')
        cifrado = False
        
    return cifrado


#========== Envio de los archivos cifrado al servidor.
def envioArchivos():
    print('Enviando Archivos.............................')
    ruta = 'C:/Users/beto_/Documents/ServicioSocial/ArchivoOpen'
    archivos = os.listdir(ruta+'/ArchivoParaEnviar/')

    if archivos:
        try:
            session = paramiko.SSHClient()
            session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            session.load_system_host_keys()
            key_file = paramiko.RSAKey.from_private_key_file('C:/Users/beto_/Documents/ServicioSocial/SSHconection/id_rsa','holamundo')
            session.connect(
                hostname='192.168.1.158',
                username='root',
                pkey=key_file,
                allow_agent=False,
                look_for_keys=False
            )
            #Se crea una instaciona de SCP cliente para el transporte de archivos.
            with scp.SCPClient(session.get_transport()) as scps:
                for file in archivos:
                    scps.put(ruta+'/ArchivoParaEnviar/'+file, '/root/carpetaEnvio/'+file) # Copy my_file.txt to the server
                    os.remove(ruta+'/ArchivoParaEnviar/'+file)
                print('Archivos enviados.')
                envio = True
        except:
            print('Error: No se puede enviar archivos la servidor.')
            envio = False
    else:
        print('No existe archivos para enviar.')
        envio = False

    return envio

def exeCommand():
    print("Ejecutando comando...............")
    try:
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.load_system_host_keys()

        key_file = paramiko.RSAKey.from_private_key_file('C:/Users/beto_/Documents/ServicioSocial/SSHconection/id_rsa','holamundo')

        session.connect(
            hostname='192.168.1.158',
            username='root',
            pkey=key_file,
            allow_agent=False,
            look_for_keys=False
        )

        stdin,stdout,stderr=session = session.exec_command("python3 /root/sshkey.py")

        stdout = stdout.read()
        res = stdout.decode()

        if res:
            res = res.replace('\n','')
            if res == 'True':
                print("Comando Ejecutado.")
            else:
                print("Error: No se peude enviar los archivos.")
        else:
            print("Error: No se puede ejecutar el comando")

        stdin.close()
    except:
        print("Error: No se puede ejecutar el comando")
    

def procesoPrincipal():
    ext = extracccion()
    if ext == True:
        cifrado = cifradoPGP()
        if cifrado == True:
            envio = envioArchivos()
            if envio == True:
                exeCommand()

    print('Termina proceso de cifrado.')


procesoPrincipal()