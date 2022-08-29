from datetime import datetime
from dbconnections import DB_conection
from intel_connection import intelligence
from people_connections import people_connection
from products_connections import products_connection

class sales(DB_conection):
    def __init__(self, user, passwd, table = 'ventas'):
        super().__init__(table)
        self.user  = user
        self.__passwd = passwd
        self.table = table
        self.data_customer = people_connection()
        self.data_product  = products_connection()
        
        self.data_customer.connect_to_DB(self.user, self.__passwd)
        self.data_product.connect_to_DB(self.user, self.__passwd)
        self.connect_to_DB(self.user, self.__passwd)
    
    def find_customer(self, customer_code):
        query = f'''
            select nombre, telefono, deuda 
            from {self.data_customer.table} 
            where codigo_cliente = {customer_code} 
        '''
        return self.data_customer.run_query(query)[0]

    def find_product(self, product_code):
        query = f'''
            select Descripcion, Precio, Cantidad, ITBIS
            from {self.data_product.table} 
            where codigo = {product_code} 
        '''
        return self.data_product.run_query(query)[0]

    def check_in(self, id_venta, customer_code, value, payment, items):
        self.id       = id_venta
        self.cus_code = customer_code
        self.value    = value
        self.payment  = payment
        self.items    = items

        query = f'''
            INSERT INTO {self.table}
                (venta_no,
                Fecha,
                Vendedor, 
                codigo_cliente, 
                Valor, 
                Forma_de_pago, 
                Detalle_items) 
            VALUES 
                ('{self.id}', 
                '{datetime.now()}', 
                '{self.user}', 
                '{self.cus_code}', 
                {self.value}, 
                '{self.payment}', 
                '{self.items}')
        '''
        self.run_query(query)

    def update_inventory(self, codes, qtys, prices):
        intel = intelligence(self.id)
        intel.connect_to_DB(self.user, self.__passwd)

        try:
            new_info = zip(codes, qtys, prices)

            for i in new_info:
                self.data_product.sell_product(i[0], i[1])
                intel.add_intel(self.cus_code, i[0], i[1],i[2])
                
        except:
            self.data_product.sell_product(codes, qtys)
            intel.add_intel(self.cus_code, codes, qtys, prices)


if __name__ == '__main__':
    pass