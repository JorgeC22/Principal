import paramiko
import os
import scp

#=======Envio de archivos a la caja toka.
#proceso encargado de enviar los archivos cifrados a la caja toka.
def envioArchivostoka():
    #Ruta donde esta ubicado el proyecto en su general.
    ruta = '/home/ubuntu'
    #Se obtiene una lista de nombres de los archivos sobre el directorio indicado (carpetaEnvioPGP).
    archivos = os.listdir(ruta+'/carpetaEnvio/')

    #Si existe una lista de archivos inicia el proceso de envio.
    if archivos:
        try:
            #Se crea un objeto SSH cliente para realizar la conexion con la instancia/servidor.
            session = paramiko.SSHClient()
            session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            session.load_system_host_keys()
            
            #Se realiza la conexion con la instancia implementando la clave SSH.
            session.connect(
                hostname='',
                username='',
                password=''    
            )
            
            #Se crea una instaciona de SCP cliente para el transporte de archivos.
            with scp.SCPClient(session.get_transport()) as scps:
                for file in archivos:
                    scps.put(ruta+'/carpetaEnvio/'+file, '/home/tokaprocesadora/alquimia/output/'+file) # Copia de los archivos a la instancia toka.
                    os.remove(ruta+'/carpetaEnvio/'+file) #se elimina el archivo que ya fue copiado.
                envio = True #indica que se han enviado todos los archivos.
        except:
            envio = False #indica que no se pudieron enviar los archivos.
    else:
        envio = False #indica que no existen archivos en la carpeta o no se pudieron enviar los archivos.

    return envio

enviotoka = envioArchivostoka() #se ejecuta el proceso de envio de archivo a toka.
if enviotoka: # si obtion un resultado diferente a False entonces se manda a imprimir la cadena true
                # a pantalla para la evaluacion de resultados desde el script cifradoPGPcompleto.py
    print('True')
else: #si el resultado es False sigue el mismo proceso con la cadena False.
    print('False')