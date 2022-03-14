from paramiko import SSHClient, RSAKey, AutoAddPolicy

def extracccion():
    session = SSHClient()
    session.set_missing_host_key_policy(AutoAddPolicy())
    session.load_system_host_keys()

    key_file = RSAKey.from_private_key_file('')

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
    if list:
        print('Existe una lista de archivos.')
        for x in list:
            cadena = x.find('.PGP')
            if cadena != -1:
                list2.append(x)

    print(list2)
    
    if list2:
        print('Existe Archivos.')
        print(list2)
        for x in list2:
            sftp_client.get('/home/ec2-user/archivos_26_01_2022/'+x,x)
    else:
        print('No existe archivos.')
    
    sftp_client.close()
    session.close()

extracccion()