from main_features.start_module import run
run()

import tkinter as tk
from main_features.GUI_elements.tables import Table
from tkinter import messagebox
from main_features.frames import Frame
from main_features.sales_connection import sales
from main_features.GUI_elements.buttons import button
from main_features.GUI_elements.labels_entries import collector

def invoices(root, name, passwd):
    # Create frame
    data = sales(name, passwd)
    frame = Frame(root)
    frame.config(background = '#fcfcfc')
    
    ## Input labels
    customer_code = collector(frame, 'Codigo de Cliente :', 1, start_here = True)
    customer_name = collector(frame, 'Nombre :', 2)
    customer_debt = collector(frame, 'Deuda :', 3)
    customer_cont = collector(frame, 'Contacto :', 4)

    code        = collector(frame, 'Código :', 1, displace = 3)
    description = collector(frame, 'Descipción :', 2, displace = 3)
    price       = collector(frame, 'Precio :', 3, displace = 3)
    quantity    = collector(frame, 'Cantidad :', 4, displace = 3)
    value       = collector(frame, 'Subtotal: ', 5, displace = 3)

    customer_code.field_entry.config(width = 40)
    customer_name.field_entry.config(width = 40, state = 'disabled')
    customer_debt.field_entry.config(width = 40, state = 'disabled')
    customer_cont.field_entry.config(width = 40, state = 'disabled')
    code.field_entry.config(width = 40)       
    description.field_entry.config(width = 40)
    price.field_entry.config(width = 40)
    quantity.field_entry.config(width = 40)
    value.field_entry.config(width = 40)

    headers_product = ['Código', 'Descripción', 'Precio', 'Cantidad', 'Subtotal']
    item_list = Table(frame, headers_product, 7, 4, 5, 'green_table', rows_qty = 18)
    item_list.grid(column = 2)
    item_list.column(headers_product[0], width = 200)
    item_list.column(headers_product[1], width = 500)
    item_list.column(headers_product[2], width = 100, anchor = tk.E)
    item_list.column(headers_product[3], width = 100, anchor = tk.E)
    item_list.column(headers_product[4], width = 150, anchor = tk.E)


    def search_customer():
        if len(customer_code.value.get()):
            
            cust = data.find_customer(customer_code.value.get())    
            customer_name.value.set(cust[0])
            customer_debt.value.set(cust[1])
            customer_cont.value.set(cust[2])
            code.field_entry.focus()

        else:
            code.field_entry.focus()

    def add_product():
        search_customer()
        if len(code.value.get()):
            n = len(item_list.get_children())
            prod = data.find_product(code.value.get())
            ans = (code.value.get(),
                    prod[0], 
                    prod[1],
                    1, 
                    prod[1]
            )
            item_list.insert('', tk.END, values = ans, tag = data.row_parity(n))
            code.value.set('')
            code.field_entry.focus()
    
    def edit_selection():
        pass

    search   = button(frame, 'Buscar cliente', search_customer, 'blue_button', (6, 2))            
    add_item = button(frame, 'Agregar producto', add_product, 'green_button', (6, 5)) 
    root.bind('<Return>', lambda event: add_product())
      


if __name__ == '__main__':
    root  = tk.Tk()
    frame = invoices(root, 'comercial_auyama_boss', '8498731104+1')
    root.state('zoomed')
    #root.resizable(False, False)
    root.mainloop()