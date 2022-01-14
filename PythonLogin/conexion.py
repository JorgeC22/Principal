import pymysql

def conect():
    return pymysql.connect(host='localhost',
                            user='root',
                            password='12345',
                            db='peliculas')
