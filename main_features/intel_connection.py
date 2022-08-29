import uuid
from dbconnections import DB_conection

class intelligence(DB_conection):

    def __init__(self, uuid_sells,table = 'bussines_intelligence'):
        super().__init__(table)
        self.table = table
        self.id    = uuid_sells


    def add_intel(self, customer_code, product_code, qty, price):
        
        self.cus_code = customer_code
        self.pro_code = product_code
        self.qty      = qty
        self.price    = price

        query = f'''
        INSERT INTO {self.table} (Transaccion,
                                    evento_venta,
                                    codigo_cliente, 
                                    codigo_producto, 
                                    cantidad, 
                                    precio)
        VALUES
            ('{uuid.uuid1().hex}',
            '{self.id}',
            '{self.cus_code}', 
            '{self.pro_code}', 
             {self.qty},
             {self.price})
        '''
        self.run_query(query)

if __name__ == '__main__':
    pass