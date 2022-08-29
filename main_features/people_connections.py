from dbconnections import DB_conection
import tkinter as tk

class people_connection(DB_conection):
    def __init__(self, table  = 'listado_de_clientes'):
        super().__init__(table)
        self.table  = table

    def get_people(self, table):

        records = table.get_children()
        for element in records:
            table.delete(element)

        # Getting new information
        query  = f'select * from {self.table} order by codigo_cliente asc'
        dbrows = self.run_query(query) 
        parity = 0

        for row in dbrows:
            parity+=1
            code = row[0] 
            name = row[1]
            phne = row[2]
            debt = "{:.2f}".format(row[3]) 
            home = row[4]
            mail = row[5]
            ans  = (code, name, phne, debt, home, mail)
            table.insert('', tk.END, values = ans, tag = self.row_parity(parity))

    def add_customer(self, code, name, phone, debt, home, email):
        self.code        = code
        self.name        = name
        self.phone       = phone
        self.debt        = debt
        self.home        = home
        self.email       = email

        query = f'''
        INSERT INTO {self.table} (codigo_cliente, 
                                  nombre, 
                                  telefono, 
                                  deuda, 
                                  direccion, 
                                  correo_electronico)
        VALUES
            ('{self.code}', 
            '{self.name}', 
            '{self.phone}',
            {self.debt}, 
            '{self.home}',
            '{self.email}')
        '''
        self.run_query(query)

    def edit_customer(self, code, name, phone, debt, home, email):
        self.code        = code
        self.name        = name
        self.phone       = phone
        self.debt        = debt
        self.home        = home
        self.email       = email

        query = f'''
        UPDATE {self.table}
        SET 
            nombre = "%s", 
            telefono = "%s", 
            deuda = "%s", 
            direccion = "%s", 
            correo_electronico = "%s"
        WHERE 
            codigo_cliente = "%s"
        '''%(
            self.name,
            self.phone,
            self.debt,
            self.home,
            self.email, 
            self.code)
        self.run_query(query)

    def delete_customer(self, code):

        self.code = code

        query = f'''delete from {self.table} where codigo_cliente = "%s"'''%(self.code)

        self.run_query(query)


if __name__ == '__main__':
    pass