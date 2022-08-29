from main_features.start_module import run
run()

import tkinter as tk
from main_features.GUI_elements.tables import Table
from tkinter import messagebox
from main_features.frames import Frame
from main_features.people_connections import people_connection
from main_features.GUI_elements.buttons import button
from main_features.GUI_elements.labels_entries import collector

def people(root, user, passwd):

    data = people_connection()
    data.connect_to_DB(user, passwd)
    frame = Frame(root)
    frame.config(background = '#fcfcfc')
    
    code        = collector(frame, 'Código de cliente :', 1,
                            displace = -1, start_here = True)
    name        = collector(frame, 'Nombre :', 2, displace = -1)
    phone       = collector(frame, 'Telefono :', 3, displace = -1)
    debt        = collector(frame, 'Deuda :', 4, displace = -1)
    direction   = collector(frame, 'Dirección :', 5, displace = -1)
    email       = collector(frame, 'Correo electrónico :', 6, displace = -1)

    headers_product = ['Código', 'Nombre', 'Telefono', 'Deuda', 'Dirección', 'e-mail']
    people_list = Table(frame, headers_product, 10, 9, 8, 'green_table', rows_qty = 15)

    people_list.column(headers_product[0], width = 150, anchor = tk.CENTER)
    people_list.column(headers_product[1], width = 200)
    people_list.column(headers_product[2], width = 150, anchor = tk.CENTER)
    people_list.column(headers_product[3], width = 100, anchor = tk.E)
    people_list.column(headers_product[4], width = 150)
    people_list.column(headers_product[5], width = 200)

    data.get_people(people_list)

    def clean():
        code.value.set('')
        name.value.set('')
        phone.value.set('')
        debt.value.set('')
        direction.value.set('')
        email.value.set('')

    def labels_state(state):
        if state:
            var = 'normal'
            save_button['text'] = 'Guardar'
        else:
            var = 'disabled' 
            save_button['text'] = 'Crear'

        code.field_entry.config(state = var)
        name.field_entry.config(state = var)
        phone.field_entry.config(state = var)
        debt.field_entry.config(state = var)
        direction.field_entry.config(state = var)
        email.field_entry.config(state = var)

    def create_new_customer(): # Also add new line
        
        labels_state(True)
        test_code  = len(code.value.get()) > 0
        test_name  = len(name.value.get()) > 0
                
        if test_code and test_name:
            data.add_customer(
                            str(code.value.get()),
                            str(name.value.get()),
                            str(phone.value.get()),
                            "{:.2f}".format(float(debt.value.get())),
                            str(direction.value.get()),
                            str(email.value.get())
                            )

        data.get_people(people_list)
        clean()

    def update_customer():
        
        labels_state(True)
        test_code  = len(code.value.get()) > 0
        test_name  = len(name.value.get()) > 0
                
        if test_code and test_name:
            data.edit_customer(
                            str(code.value.get()),
                            str(name.value.get()),
                            str(phone.value.get()),
                            float(debt.value.get()),
                            str(direction.value.get()),
                            str(email.value.get())
                            )

        data.get_people(people_list)
        clean()

    def cancel_operation():
        labels_state(False)
        save_button.config(command = create_new_customer)
        save_button['text'] = 'Crear cliente'
        save_button.button_color('green_button')

        cancel_button['text'] = 'Cancelar'
        cancel_button.button_color('red_button')

        clean()

    def edit_customer():
        try:
            labels_state(True)
            
            save_button['text'] = 'Actualizar cliente'
            save_button.button_color('orange_button')
            save_button.config(command = update_customer)

            cancel_button['text'] = 'Finalizar edicion'
            cancel_button.button_color('purple_button')

            code.value.set(
                people_list.item(people_list.selection(), option = 'values')[0])
            name.value.set(
                people_list.item(people_list.selection(), option = 'values')[1])
            phone.value.set(
                people_list.item(people_list.selection(), option = 'values')[2])
            debt.value.set(
                people_list.item(people_list.selection(), option = 'values')[3])
            direction.value.set(
                people_list.item(people_list.selection(), option = 'values')[4])
            email.value.set(
                people_list.item(people_list.selection(), option = 'values')[5])
        
        except:
            messagebox.showwarning('Error de selección', 
                    'Por favor seleccione un registro y luego presione el boton editar.')
            messagebox.showwarning('Modo edicion activado', 
                    "Para crear nuevos registros presione el botón 'Finalizar edición'.")

    def delete_customer():

        try:
            customer      = people_list.item(people_list.focus(), option = 'values')[0]
            customer_name = people_list.item(people_list.focus(), option = 'values')[1] 
            
            data.delete_customer(customer) 
            data.get_people(people_list)    
            clean() 

            messagebox.showwarning('Alerta de borrado.', 
                f'El cliente >>>{customer}<<<\n"{customer_name}" \n ha sido eliminado de lod registros.')

        except tk._tkinter.TclError:
            messagebox.showwarning('Alerta de borrado.', 
                f'Solo se permite borrar un elemento a la vez.')
            

    # Buttons
    save_button   = button(frame, 'Crear cliente', 
                            create_new_customer, 'green_button', (9, 1))
    cancel_button = button(frame, 'Cancelar', cancel_operation, 'red_button', (9, 2))
    edit_button   = button(frame, 'Editar', edit_customer, 'blue_button', (11,1))
    delete_button = button(frame, 'Eliminar', delete_customer, 'black_button', (11,2))
    cancel_operation()

if __name__ == '__main__':
    pass