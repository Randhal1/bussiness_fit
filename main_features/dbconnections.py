import mysql.connector as sql
from tkinter import messagebox

class DB_conection:
    def __init__(self,
                table = 'inventario_de_productos',
                dbname = 'comercial_las_auyamas',
                host   = 'localhost'):
        self.dbname = dbname
        self.host   = host
        self.table  = table

    def connect_to_DB(self, user, passwd):

        self.user     = user
        self.__passwd = passwd

        try:
            mycon = sql.connect(host = self.host, user = self.user,
                                passwd = self.__passwd, db = self.dbname)
            if mycon.is_connected():
                self.user   = self.user
                self.__passwd = self.__passwd
        except:
            pass

    def run_query(self, query, parameters = ()):
    
        try:
        # mycon is the conection to database
            with sql.connect(host = self.host, user = self.user,
                            passwd = self.__passwd, db = self.dbname) as mycon:
                cursor = mycon.cursor()
                cursor.execute(query, parameters)
                records = cursor.fetchall() 
                mycon.commit()
            return records

        except:
            messagebox.showerror('Ejecucion fallida',
                'Hubieron errores en el query. Verificar permisos del usuario')
    
    def row_parity(self, row_number):
        if row_number % 2 == 0:
            return 'even'
        else:
            return 'odd'

if __name__ == '__main__':
    pass