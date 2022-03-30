import mariadb
import sys

class dbMDT():
    def __init__(self):
        try:
            self.conn = mariadb.connect(
                user="",
                password="",
                host="",
                port= ,
                database="",
                autocommit=True
            )
        except mariadb.Error as e:
            print(f"Error en conexión a base de datos: {e}")
            sys.exit(1)

    def insertaRegistro(self, **params):   
        try:
            self.cur = self.conn.cursor(dictionary=True, prepared=True)
            self.cur.execute("""
                INSERT INTO mdt3 (Clave_de_Trx, Tipo_de_Trx, Fecha_Origen, Fecha_Posteo, Hora, Banco_Emisor, Banco_Adquirente, Numero_de_Cuenta, 
                        Cuenta_Token, Numero_de_Autorizacin, Monto, Numero_de_Referencia, CR, Origen_Respuesta, Red_Logica_Emisor, Red_Logica_Adquirente, 
                        PSEM, Clase_de_Tarjeta, Tipo_de_Tarjeta, Aut_Cap, Comercio, Origen_Mensaje, Protocolo, Terminal_Id, Terminal_Num, 
                        Flag_Service_Code, Terminal_Capability, Nombre_comercio, Tkn_Q1_S1, Tkn_Q1_S2, Tkn_Q2_S1, Tkn_C0_S1, Tkn_C0_S2, Tkn_C0_S3, 
                        Tkn_C0_S4, Tkn_C0_S5, Tkn_C0_S6, Tkn_C0_S7, Tkn_C0_S8, Tkn_C0_S9, Tkn_C0_S10, Tkn_C0_S11, Tkn_C0_S12, Tkn_C4_S1, Tkn_C4_S2, 
                        Tkn_C4_S3, Tkn_C4_S4, Tkn_C4_S5, Tkn_C4_S6, Tkn_C4_S7, Tkn_C4_S8, Tkn_C4_S9, Tkn_C4_S10, Tkn_C4_S11, Tkn_C4_S12, Tkn_04_S1, 
                        Tkn_04_S2, Tkn_04_S3, Tkn_04_S4, Tkn_04_S5, Tkn_04_S6, Tkn_Q6_S1, Tkn_Q6_S2, Tkn_Q6_S3, Tkn_C6_S1, Tkn_C6_S2, Tkn_CE_S1, 
                        Tkn_CE_S2, Tkn_B2_S3, Tkn_B2_S4, Tkn_B2_S5, Tkn_B2_S6, Tkn_B2_S7, Tkn_B2_S8, Tkn_B2_S9, Tkn_B2_S10, Tkn_B2_S11, Tkn_B2_S12, 
                        Tkn_B2_S13, Tkn_B2_S14, Tkn_B2_S16, Tkn_B3_S2, Tkn_B3_S3, Tkn_B3_S6, Tkn_B3_S7, Tkn_B3_S8, Tkn_B3_S10, Tkn_B4_S1, Tkn_B4_S2, 
                        Tkn_B4_S3, Tkn_B4_S4, Tkn_B4_S5, Tkn_B4_S6, Tkn_B4_S7, Tkn_B4_S8, Tkn_B4_S9, Tkn_B5_S1, Tkn_B5_S2, Tkn_B5_S3, Tkn_B5_S4, Tkn_B5_S5, cod_registro)
                        VALUES
                        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                """,params['tuplaDatos'])
        except mariadb.ProgrammingError as e:
            print(f"Error insertando registro: {e}")
        except mariadb.InterfaceError as e:
            print(f"Desconexión a BD log: {e}")

    def existeRegistro(self, i):
        try:
            self.cur = self.conn.cursor(dictionary=True, prepared=True)
            self.cur.execute("SELECT COUNT(*) as cuenta FROM mdt3 WHERE cod_registro = '%s'; "% i[101])
            record = self.cur.fetchone()   
            self.cur.close()
            return record
        except mariadb.ProgrammingError as e:
            print(f"Error consultando existencia de registro: {e}")
        except mariadb.InterfaceError as e:
            print(f"Desconexión a BD log: {e}")

def dbUsuario():
    return mariadb.connect(
        host="",
        port= ,
        user="",
        passwd="",
        database=""
    )