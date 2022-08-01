import mysql.connector as sql
import tkinter as tk

class DB_conection:
    def __init__(self, 
                dbname = 'comercial_las_auyamas',
                host   = 'localhost',
                user   = 'Comercial_auyama_adm',
                passwd = '8498731104+1',
                table  = 'inventario_de_productos'):
        self.dbname = dbname
        self.host   = host
        self.user   = user
        self.passwd = passwd
        self.table  = table

    def run_query(self, query, parameters = ()):

        # mycon is the conection to database
        with sql.connect(host = self.host, user = self.user,
                            passwd = self.passwd, db = self.dbname) as mycon:
            cursor = mycon.cursor()
            cursor.execute(query, parameters)
            records = cursor.fetchall() 
            mycon.commit()
        return records

    def get_products(self, table):

        # Cleaning the table
        records = table.get_children()
        for element in records:
            table.delete(element)

        # Getting new information
        query  = f'select * from {self.table} order by codigo asc'
        dbrows = self.run_query(query) 
        
        for row in dbrows:
            table.insert('', tk.END, values = row)

    def add_product(self, code, description, cost, price, qty):
        self.code        = code
        self.description = description
        self.cost        = cost
        self.price       = price
        self.qty         = qty

        query = f'''
        INSERT INTO {self.table} (Codigo, Descripcion, Costo, Precio, Cantidad)
        VALUES
            ('{self.code}', '{self.description}', {self.cost}, {self.price}, {self.qty})
        '''
        self.run_query(query)


if __name__ == '__main__':
    pass