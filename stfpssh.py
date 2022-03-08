import pysftp
 
conexion = pysftp.Connection(host='192.168.1.153',username='root',password='')
conexion.put('PGPSTFP.py','/root/PGPSTFP.py')
conexion.close()

