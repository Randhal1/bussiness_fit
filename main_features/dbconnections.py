import mysql.connector as sql
import tkinter as tk
from tkinter import messagebox

class DB_conection:
    def __init__(self,
                table,
                dbname = 'comercial_las_auyamas',
                host   = 'localhost',
                user   = 'comercial_auyama_boss',
                passwd = '8498731104+1'):
        self.dbname = dbname
        self.host   = host
        self.user   = user
        self.passwd = passwd
        self.table  = table

    def run_query(self, query, parameters = ()):
    
        try:
        # mycon is the conection to database
            with sql.connect(host = self.host, user = self.user,
                                passwd = self.passwd, db = self.dbname) as mycon:
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