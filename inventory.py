from main_features.start_module import run
run()

import tkinter as tk
from main_features.GUI_elements.tables import Table
from tkinter import messagebox
from main_features.frames import Frame
from main_features.products_connections import products_connection
from main_features.GUI_elements.buttons import button
from main_features.GUI_elements.labels_entries import collector

def products(root, name, passwd):
    # Create frame
    data = products_connection()
    data.connect_to_DB(name, passwd)
    frame = Frame(root)
    frame.config(background = '#fcfcfc')
    
    ## Input labels
    code        = collector(frame, 'Código :', 1, start_here = True)
    description = collector(frame, 'Descipción :', 2)
    cost        = collector(frame, 'Costo :', 3)
    price       = collector(frame, 'Precio :', 4)
    quantity    = collector(frame, 'Cantidad :', 5)

    # The list with the products
    headers_product = ['Código', 'Descripción', 'Costo', 'Precio', 'Cantidad']
    inventory_list = Table(frame, headers_product, 7, 4, 3, 'blue_table')

    inventory_list.column(headers_product[0], width = 200)
    inventory_list.column(headers_product[1], width = 500)
    inventory_list.column(headers_product[2], width = 100, anchor = tk.E)
    inventory_list.column(headers_product[3], width = 100, anchor = tk.E)
    inventory_list.column(headers_product[4], width = 100, anchor = tk.E)

    data.get_products(inventory_list)

    # Buttons section for product and define buttons operations
    def clean():
        code.value.set('')
        description.value.set('')
        cost.value.set('')
        price.value.set('')
        quantity.value.set('')

    def labels_state(state):
        if state:
            var = 'normal'
            save_button['text'] = 'Guardar'
        else:
            var = 'disabled' 
            save_button['text'] = 'Crear'

        code.field_entry.config(state = var)
        description.field_entry.config(state = var)
        cost.field_entry.config(state = var)
        price.field_entry.config(state = var)
        quantity.field_entry.config(state = var)
        cancel_button.config(state = var)

    def create_new_product(): # Also add new line
        
        labels_state(True)
        test_code  = len(code.value.get()) > 0
        test_desc  = len(description.value.get()) > 0
                
        if test_code and test_desc:
            data.add_product(
                            str(code.value.get()), 
                            str(description.value.get()), 
                            float(eval(cost.value.get())), 
                            float(eval(price.value.get())), 
                            float(eval(quantity.value.get()))
                            )

        data.get_products(inventory_list)
        clean()

    def update_product():
        
        labels_state(True)
        test_code  = len(code.value.get()) > 0
        test_desc  = len(description.value.get()) > 0
                
        if test_code and test_desc:
            data.edit_product(
                            str(code.value.get()), 
                            str(description.value.get()), 
                            float(eval(cost.value.get())), 
                            float(eval(price.value.get())), 
                            float(eval(quantity.value.get()))
                            )

        data.get_products(inventory_list)
        clean()

    def cancel_operation():
        labels_state(False)
        save_button.config(command = create_new_product)
        save_button['text'] = 'Crear'
        save_button.button_color('green_button')

        cancel_button['text'] = 'Cancelar'
        cancel_button.button_color('red_button')

        clean()

    def edit_item():
        try:
            labels_state(True)
            
            save_button['text'] = 'Actualizar'
            save_button.button_color('orange_button')
            save_button.config(command = update_product)

            cancel_button['text'] = 'Finalizar edicion'
            cancel_button.button_color('purple_button')

            code.value.set(
                inventory_list.item(inventory_list.selection(), option = 'values')[0])
            description.value.set(
                inventory_list.item(inventory_list.selection(), option = 'values')[1])
            cost.value.set(
                inventory_list.item(inventory_list.selection(), option = 'values')[2])
            price.value.set(
                inventory_list.item(inventory_list.selection(), option = 'values')[3])
            quantity.value.set(
                inventory_list.item(inventory_list.selection(), option = 'values')[4])
        except:
            messagebox.showwarning('Error de selección', 
                    'Por favor seleccione un registro y luego presione el boton editar.')
            messagebox.showwarning('Modo edicion activado', 
                    "Para crear nuevos registros presione el botón 'Finalizar edición'.")

    def delete_item():

        try:
            element   = inventory_list.item(inventory_list.focus(), option = 'values')[0]
            elmnt_dsc = inventory_list.item(inventory_list.focus(), option = 'values')[1] 
            
            data.delete_product(element) 
            data.get_products(inventory_list)    
            clean() 

            messagebox.showwarning('Alerta de borrado.', 
                f'El producto >>>{element}<<< \n "{elmnt_dsc}" \n ha sido borrado del registro.')

        except tk._tkinter.TclError:
            messagebox.showwarning('Alerta de borrado.', 
                f'Solo se permite borrar un elemento a la vez.')
            

    # Buttons
    save_button   = button(frame, 'Crear', create_new_product, 'green_button', (6, 2))
    cancel_button = button(frame, 'Cancelar', cancel_operation, 'red_button', (6, 3))
    edit_button   = button(frame, 'Editar', edit_item, 'blue_button', (8,0))
    delete_button = button(frame, 'Eliminar', delete_item, 'black_button', (8,1))
    
    cancel_operation()
    

if __name__ == '__main__':
    pass