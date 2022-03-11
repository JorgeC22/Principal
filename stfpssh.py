import pysftp
 
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


conexion = pysftp.Connection(host='192.168.1.156',username='root',password='12345', cnopts=cnopts)
conexion.put('C:/Users/beto_/Documents/ServicioSocial/SSHconection/scripts_python_ohio.pem','/root/scripts_python_ohio.pem')
conexion.close()

