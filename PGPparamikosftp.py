from paramiko import SSHClient, RSAKey

def extracccion():
    session = SSHClient()

    session.load_system_host_keys()

    key_file = RSAKey.from_private_key_file('nombre o ruta del archivo clave ssh')

    session.connect(
        hostname='',
        username='',
        pkey=key_file,
        allow_agent=False,
        look_for_keys=False
    )

    sftp_client = session.open_sftp()

    #sftp_client.put('C:/Users/beto_/Documents/ServicioSocial/Cifradotoka/archivos_26_01_2022.zip','/home/ec2-user/archivos_26_01_2022.zip')

    list = sftp_client.listdir('/home/ec2-user/archivos_26_01_2022')
    list2 = []
    print(list)
    for x in list:
        cadena = x.find("PGP")
        if cadena != -1:
            list.append(x)

    print(list2)

    if list2:
        print('Existe Archivos.')
        print(list2)
        for x in list2:
            sftp_client.get('/home/ec2-user/archivos_26_01_2022/'+x,'C:/Users/beto_/Documents/ServicioSocial/ArchivoOpen/pruebas/'+x)
    else:
        print('No existe archivos.')

    sftp_client.close()
    session.close()

extracccion()