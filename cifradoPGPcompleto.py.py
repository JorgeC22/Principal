import paramiko
import os
import gnupg
import scp

#========== Extraccion de archivo del servidor.
#proceso encargado de verificar si existen archivos y extraerlos hacia la maquina local.
def extracccion():
    print('Buscando Archivos........................')
    #Se crea un objeto SSH cliente para realizar la conexion con la instancia.
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.load_system_host_keys()

    #Se lee y almacena en la variable key_file la clave SSH sobre la intancia a conectar.
    key_file = paramiko.RSAKey.from_private_key_file('ruta/nombre del archivo clave ssh')

    #Se realiza la conexion con la instancia implementando la clave SSH.
    session.connect(
        hostname='ec2-3-143-69-212.us-east-2.compute.amazonaws.com',
        username='ubuntu',
        pkey=key_file,
        allow_agent=False,
        look_for_keys=False
    )

    #Se abre una session SFTP.
    sftp_client = session.open_sftp()

    #Se verifica existan archvios sobre el directorio indicado.
    list = sftp_client.listdir('/home/ubuntu/carpetaArchivosPGP')
    list2 = []
    
    #Si se obtiene una lista de nombres de archivos se aplica un filtro para obtener solamente archivos con extension .PGP y se crea nueva lista. 
    if list:
        print('Existe una lista de archivos.')
        for x in list:
            cadena = x.find('.PGP')
            if cadena != -1:
                list2.append(x) #se agrega nombre del archivo con la extension especificado a la nueva lista.

    #Si se crea la nueva lista de archivos se inicia el proceso de extraccion de archivos.
    if list2:
        print('Existe archivos a cifrar.')
        print('Extrallendo Archivos......................')
        for x in list2:
            sftp_client.get('/home/ubuntu/carpetaArchivosPGP'+x,'./ArchivoRecibidos/'+x) #Copia de archivos a maquina local.
            stdin,stdout,stderr = session.exec_command("rm /home/ubuntu/carpetaArchivosPGP"+x) #elimina en la instancia/servior remoto los archivos ya extraidos.
        print('Archivos Extraidos.')
        extraccion = True
    else:
        print('No Existen archivos a cifrar.')
        extraccion = False
    
    sftp_client.close()
    return extraccion

#========== Cifrado de los archivos extraidos.
#proceso encargado de decifrar y cifrar los archivos obtenidos de la instancia/servidor.
def cifradoPGP():
    print('Cifrando archivos............................')
    #Ruta donde esta ubicado el proyecto en su general.
    ruta = '/home/ubuntu'
    #Se obtiene una lista de nombres de los archivos sobre el directorio indicado (ArchivoRecibidos).
    contenido = os.listdir(ruta+'/ArchivoRecibidos/')

    #Si se obtiene una lista de archivos se inicia el proceso de descifrado y cifrado.
    if contenido:
        try:
            for x in contenido:
                #Se crea nuevo nombre de archivo cambiando la extension del mismo para el envio de archivos.
                file = x.replace('.PGP','.gpg')

                #Ser recomienda ubicar el archivo y la claves en el mismo directorio para las pruebas.
                #Se indica la ruta donde se encuaentra las claves a utilizar
                gpg = gnupg.GPG(gnupghome = ruta)
                #Se importa clave publica para el descifrado
                key_data = open(ruta+'/secret-key-DFBF0E94.asc').read()
                import_result = gpg.import_keys(key_data)

                #Se abre el archivo para cifrar el contenido, si se ubica en otra lado introducir ruta de la ubicacion.
                with open(ruta+'/ArchivoRecibidos/'+x, 'rb') as f:
                    #Se descifra el contenido y es introducido en un nuevo archivo con extension .txt
                    status = gpg.decrypt_file(f, passphrase='1cG65xIyJj4Y5E98IRhscNIYP', output= ruta+'/'+x+'.txt')

                

                #Se importa clave Toka
                key_data = open(ruta+'/public-F40B9901.pgp').read()
                import_result = gpg.import_keys(key_data)
                

                #Se abre el archivo para cifrar el contenido, si se ubica en otra lado introducir ruta de la ubicacion
                with open(ruta+'/'+x+'.txt', 'rb') as f:
                    #Se cifra el contenido y es introducido en un nuevo archivo dentro la carpeta ArchivoParaEnviar.
                    status = gpg.encrypt_file(f, recipients=import_result.fingerprints[0], armor=False, always_trust=True, output= ruta+'/ArchivoParaEnviar/'+file)


                #Se elimina el archivo cifrado de la carpeta ArchivoRecibidos.
                os.remove(ruta+'/ArchivoRecibidos/'+x)
                #Se elimina el archivo obtenida al decifrar el original.
                os.remove(ruta+'/'+x+'.txt')
            print('Archivos Cifrados correctamente.')
            #indica que el cifrado se ejecuto correctamente.
            cifrado = True
        except:
            print('Error: No se pueden cifrar los archivos.')
            #indica que el cifrado no pudo realizarse.
            cifrado = False
    else:
        print('No existen archivos a cifrar.')
        #indica que no existe archivos en el directorio o cifrado no pudo realizarse.
        cifrado = False
        
    return cifrado


#========== Envio de los archivos cifrado al servidor.
#proceso encargado de enviar los archivos cifrados a la instancia/servidor.
def envioArchivos():
    print('Enviando Archivos.............................')
    #Ruta donde esta ubicado el proyecto en su general.
    ruta = '/home/ubuntu'
    #Se obtiene una lista de nombres de los archivos sobre el directorio indicado (ArchivoParaEnviar).
    archivos = os.listdir(ruta+'/ArchivoParaEnviar/')

    #Si existe una lista de archivos inicia el proceso de envio.
    if archivos:
        try:
            #Se crea un objeto SSH cliente para realizar la conexion con la instancia/servidor.
            session = paramiko.SSHClient()
            session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            session.load_system_host_keys()

            #Se lee y almacena en la variable key_file la clave SSH sobre la intancia a conectar.
            key_file = paramiko.RSAKey.from_private_key_file('C:/Users/beto_/Documents/ServicioSocial/SSHconection/id_rsa','holamundo')
            
            #Se realiza la conexion con la instancia implementando la clave SSH.
            session.connect(
                hostname='ec2-3-143-69-212.us-east-2.compute.amazonaws.com',
                username='ubuntu',
                pkey=key_file,
                allow_agent=False,
                look_for_keys=False
            )
            #Se inicia sesion SCP cliente para el transporte de archivos.
            with scp.SCPClient(session.get_transport()) as scps:
                for file in archivos:
                    scps.put(ruta+'/ArchivoParaEnviar/'+file, '/home/ubuntu/carpetaEnvioPGP/'+file) # Copia del archivo a la instancia/servidor.
                    os.remove(ruta+'/ArchivoParaEnviar/'+file) #Se elimina el archivo que ya fue copiado en la instancia/servidor.
                print('Archivos enviados.')
                envio = True #indica si el envio de archivos se ejecuto correactamente.
        except:
            print('Error: No se puede enviar archivos la servidor.')
            envio = False #indica si no se pudo realizar el envio de archivos.
    else:
        print('No existe archivos para enviar.')
        envio = False #Indica que no existen archivos en el directorio o no se pudo realizar el envio.

    return envio

#=====================Ejecucion de Comandos Remoto.
#proceso encargado de ejecutar el script ubicado en la instancia/servidor.
def exeCommand():
    print("Ejecutando comando...............")
    try:
        #Se crea un objeto SSH cliente para realizar la conexion con la instancia/servidor.
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.load_system_host_keys()

        #Se lee y almacena en la variable key_file la clave SSH sobre la intancia a conectar.
        key_file = paramiko.RSAKey.from_private_key_file('ruta/nombre del archivo clave ssh')

        #Se realiza la conexion con la instancia implementando la clave SSH.
        session.connect(
            hostname='ec2-3-143-69-212.us-east-2.compute.amazonaws.com',
            username='ubuntu',
            pkey=key_file,
            allow_agent=False,
            look_for_keys=False
        )

        #se ejecuta comando(ejecucion de script python) dentro de la instancia/servidor y se obtenienen tres resultados entrada,salida y error.
        stdin,stdout,stderr=session = session.exec_command("python3 /home/ubuntu/sshtoka.py")

        #Se lee los datos obtendio en la variable stdout(salida) y se decodifica.
        stdout = stdout.read()
        res = stdout.decode()

        #si la variable contiene algun valor comienza el evaluacion del mismo.
        if res:
            res = res.replace('\n','') #se eliminan las secuencias de escape \n.
            #si la cadena obtenida es igual a True entonces el comando se ejecuto correctamente.
            if res == 'True':
                print("Comando Ejecutado.")
            else: #si la cadena obtenida es igual es diferente a True entonces el comando no se pudo ejecutar.
                print("Error: No se puede enviar los archivos.")
        else:
            #indica que no se pudo ejecutar comando ya que no obtuvo valor de salida(stdout)
            print("Error: No se puede ejecutar el comando")

        #Se cierra la entrada de comandos.
        stdin.close()
    except:
        #indica que no pudo realizar el proceso de ejecucion de comandos.
        print("Error: No se puede ejecutar el comando")
    

#=============Proceso Princial.
#Proceso encargado de ejecutar en orden todos los procesos definido anteriormente.
def procesoPrincipal():
    ext = extracccion() #se ejecuta el proceso de extraccion.
    if ext: #si la variable "ext" no obtiene un resultado entonces no se pudo realizar el proceso.
        cifrado = cifradoPGP() #se ejecuta el proceso de cifrado.
        if cifrado: #si la variable "cifrado" obtiene un resultado diferente a False entonces se ejecuto correctamente le proceso.
            envio = envioArchivos() #se ejecuta el proceso de envio de archivos.
            if envio: #si la variable "envio" obtiene un resultado diferente a False entonces se ejecuto correctamente le proceso.
                exeCommand() #se ejecuta el proceso de ejecucion de comandos remoto.

    print('Termina proceso de cifrado.')


procesoPrincipal()#se ejecuta el proceso principal para la realizacion completa del cifrado de archivos.