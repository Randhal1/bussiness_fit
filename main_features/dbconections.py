import mysql.connector as sql
import tkinter as tk
from tkinter import messagebox

class DB_conection:
    def __init__(self, 
                dbname = 'comercial_las_auyamas',
                host   = 'localhost',
                user   = 'comercial_auyama_boss',
                passwd = '8498731104+1',
                table  = 'inventario_de_productos'):
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

    def get_products(self, table):

        # Cleaning the table
        records = table.get_children()
        for element in records:
            table.delete(element)

        # Getting new information
        query  = f'select * from {self.table} order by codigo asc'
        dbrows = self.run_query(query) 

        def row_parity(row_number):
            if row_number % 2 == 0:
                return 'even'
            else:
                return 'odd'
        
        parity = 0

        for row in dbrows:
            parity+=1
            code = row[0] 
            desc = row[1]
            cost = "{:.2f}".format(row[2]) 
            prce = "{:.2f}".format(row[3]) 
            qnty = "{:.2f}".format(row[4]) 
            ans  = (code, desc, cost, prce, qnty)
            table.insert('', tk.END, values = ans, tag = row_parity(parity))

    def add_product(self, code, description, cost, price, qty):
        self.code        = code
        self.description = description
        self.cost        = cost
        self.price       = price
        self.qty         = qty

        query = f'''
        INSERT INTO {self.table} (Codigo, Descripcion, Costo, Precio, Cantidad)
        VALUES
            ('{self.code}', 
            '{self.description}', 
            {self.cost},
            {self.price}, 
            {self.qty})
        '''
        self.run_query(query)

    def edit_product(self, code, description, cost, price, qty):
        self.code        = code
        self.description = description
        self.cost        = cost
        self.price       = price
        self.qty         = qty

        # The update statement its different for security propourses, consider to update
        # all the code to make it safer 05-08-2022
        query = f'''
        UPDATE {self.table}
        SET 
            Descripcion = "%s", 
            Costo = "%s", 
            Precio = "%s",
            Cantidad = "%s"
        WHERE 
            Codigo = "%s"
        '''%(
            self.description,
            self.cost,
            self.price,
            self.qty, 
            self.code)
        self.run_query(query)

    def delete_product(self, code):

        self.code = code

        query = f'''delete from {self.table} where Codigo = "%s"'''%(self.code)
        #param = (self.code,)

        self.run_query(query)


if __name__ == '__main__':
    data = DB_conection()
    data.delete_product('1')
    #data.edit_product('155', 'El gato, aminalito bello', 3000, 5000, 40)