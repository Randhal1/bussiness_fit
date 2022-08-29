from main_features.start_module import run
run()

import tkinter as tk
import uuid
from main_features.GUI_elements.tables import Table
from main_features.frames import Frame
from main_features.sales_connection import sales
from main_features.GUI_elements.buttons import button
from main_features.GUI_elements.labels_entries import collector
from main_features.invoice_printer import print_invoice

def invoices(root, name, passwd):
    
    # Create frame
    data = sales(name, passwd)
    frame = Frame(root)
    frame.config(background = '#fcfcfc')

    # Values
    total = 0
    
    ## Input labels
    customer_code = collector(frame, 'Codigo de Cliente :', 1, start_here = True)
    customer_name = collector(frame, 'Nombre :', 2)
    customer_debt = collector(frame, 'Deuda :', 3)
    customer_cont = collector(frame, 'Contacto :', 4)

    code        = collector(frame, 'Código :', 1, displace = 2)
    description = collector(frame, 'Descipción :', 2, displace = 2)
    price       = collector(frame, 'Precio :', 3, displace = 2)
    itbis       = collector(frame, 'ITBIS :', 4, displace = 2)
    quantity    = collector(frame, 'Cantidad :', 5, displace = 2)
    value       = collector(frame, 'Subtotal :', 6, displace = 2)

    customer_code.field_entry.config(width = 20)
    customer_name.field_entry.config(width = 20, state = 'disabled')
    customer_debt.field_entry.config(width = 20, state = 'disabled')
    customer_cont.field_entry.config(width = 20, state = 'disabled')
    code.field_entry.config(width = 20)       
    description.field_entry.config(width = 20)
    price.field_entry.config(width = 20)
    itbis.field_entry.config(width = 20)
    quantity.field_entry.config(width = 20)
    value.field_entry.config(width = 20)

    headers_product = ['Código', 'Descripción', 'Precio', 'ITBIS', 'Cantidad', 'Subtotal']
    item_list = Table(frame, headers_product, 8, 4, 5, 'green_table', rows_qty = 12)
    item_list.grid(column = 1)
    item_list.column(headers_product[0], width = 100)
    item_list.column(headers_product[1], width = 300)
    item_list.column(headers_product[2], width = 100, anchor = tk.E)
    item_list.column(headers_product[3], width = 100, anchor = tk.E)
    item_list.column(headers_product[4], width = 100, anchor = tk.E)
    item_list.column(headers_product[5], width = 100, anchor = tk.E)

    total_box = collector(frame, 'Total', 25, displace = 1)
    total_box.field_entry.config(bg = '#A3E4D7')
    
    def total_amount(total):
        for subtotal in item_list.get_children():
            total += float(item_list.item(subtotal, 'values')[5])

        total_box.value.set("{:.2f}".format(total))

    def search_customer():
        if customer_code.value.get() != '':

            cust  = data.find_customer(customer_code.value.get())    
            customer_name.value.set(cust[0])
            customer_debt.value.set(cust[1])
            customer_cont.value.set(cust[2])
            code.field_entry.focus()

        else:
            code.field_entry.focus()

    def to_add(prop, default):
        if prop == '':
            return default
        else:
            return float(prop)

    def reset_form():
        code.value.set('')
        description.value.set('')
        price.value.set('')
        itbis.value.set('')
        quantity.value.set('')
        value.value.set('')

        customer_code.value.set('')
        customer_name.value.set('')
        customer_debt.value.set('')
        customer_cont.value.set('')
        
        total_box.value.set('')

        for item in item_list.get_children():
            item_list.delete(item)


    def add_product():
        code.field_entry.config(state = 'normal')       
        description.field_entry.config(state = 'normal')
        search_customer()
        if len(code.value.get()):
            n = len(item_list.get_children())
            prod = data.find_product(code.value.get())
            ans = (code.value.get(),
                    prod[0], 
                    "{:.2f}".format(to_add(price.value.get(), prod[1])),
                    "{:.2f}".format(prod[3]),
                    "{:.2f}".format(to_add(quantity.value.get(), 1)),
                    "{:.2f}".format(to_add(quantity.value.get(), 1) * to_add(price.value.get(), prod[1])))
            item_list.insert('', tk.END, values = ans, tag = data.row_parity(n))
            code.value.set('')
            description.value.set('')
            price.value.set('')
            itbis.value.set('')
            quantity.value.set('')
            value.value.set('')
            code.field_entry.focus()
            total_amount(total)


    def delete_selected_item():
        item_list.delete(item_list.selection())
        total_amount(total)
    

    def edit_selection():
        code.field_entry.config(state = 'disabled')       
        description.field_entry.config(state = 'disabled')
        code.value.set(
            item_list.item(item_list.selection(), option = 'values')[0]
        )
        description.value.set(
            item_list.item(item_list.selection(), option = 'values')[1]
        )
        price.value.set(
            item_list.item(item_list.selection(), option = 'values')[2]
        )
        itbis.value.set(
            item_list.item(item_list.selection(), option = 'values')[3]
        )
        quantity.value.set(
            item_list.item(item_list.selection(), option = 'values')[4]
        )
        value.value.set(
            item_list.item(item_list.selection(), option = 'values')[5]
        )

        delete_selected_item()


    def check_in():
        
        identifier_unique = uuid.uuid1().hex

        items  = []
        quant  = []
        prices = []

        if customer_code.value.get() == '':
            ccode = '01'
        else:
            ccode = customer_code.value.get()
        
        total = float(total_box.value.get())

        invoice_items = 'Codigo descripcion             precio      cantidad    subtotal \n'

        receipt = []

        for item in item_list.get_children():
            a = item_list.item(item, option = 'values')
            receipt.append(a)
            items.append(a[0])
            quant.append(a[3])
            prices.append(a[2])
            invoice_items += f'{a[0]:<7}{a[1]:<24}{a[2]:<12}{a[3]:<12}{a[4]:<15}\n'
        
        invoice_items += f'\n                        Total a pagar = {total}'

        # Is it needed to develop a method to change payment
        data.check_in(identifier_unique, ccode, total, 'Efectivo', invoice_items)
        data.update_inventory(items, quant, prices)

        titbi = 0

        for tax in item_list.get_children():
            titbi += float(item_list.item(tax, 'values')[3])

        
        print_invoice(name, 
                    customer_code.value.get(),
                    customer_name.value.get(),           
                    receipt, total, titbi, uuid.uuid1().hex)
        reset_form()

    search   = button(frame, 'Buscar cliente', search_customer, 'blue_button', (7, 2))            
    add_item = button(frame, 'Agregar producto', add_product, 'green_button', (7, 4)) 
    check_in_button   = button(frame, 'Facturar', check_in, 'purple_button', (26, 4))
    reset_form_button = button(frame, 'Cancelar venta', reset_form, 'red_button', (26, 3))


    root.bind('<Return>', lambda event: add_product())
    root.bind('<Escape>', lambda event: reset_form())
    item_list.bind('<Double-Button-1>', lambda x: edit_selection())
    item_list.bind('<Double-Button-3>', lambda x: delete_selected_item())


if __name__ == '__main__':
    pass