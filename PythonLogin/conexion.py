import mariadb

def conect():
    return mariadb.connect(host='localhost',
                            user='root',
                            password='12345',
                            db='visorusuarios',
                            port=3307,)
