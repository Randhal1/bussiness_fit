from dbconnections import DB_conection
import tkinter as tk

class products_connection(DB_conection):
    def __init__(self, table  = 'inventario_de_productos'):
        super().__init__(table)
        self.table  = table

    def get_products(self, table):

        # Cleaning the table
        records = table.get_children()
        for element in records:
            table.delete(element)

        # Getting new information
        query  = f'select * from {self.table} order by codigo asc'
        dbrows = self.run_query(query) 
        parity = 0

        for row in dbrows:
            parity+=1
            code = row[0] 
            desc = row[1]
            cost = "{:.2f}".format(row[2]) 
            prce = "{:.2f}".format(row[3]) 
            qnty = "{:.2f}".format(row[4]) 
            ans  = (code, desc, cost, prce, qnty)
            table.insert('', tk.END, values = ans, tag = self.row_parity(parity))

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
    pass