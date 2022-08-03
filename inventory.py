import tkinter as tk
from tkinter import ttk
from main_features.frames import Frame
from main_features.dbconections import DB_conection
from main_features.GUI_elements.buttons import button
from main_features.GUI_elements.labels_entries import collector

def products():
    # Create frame
    root = tk.Tk()
    data = DB_conection()
    frame = Frame(root)
    
    ## Input labels
    code        = collector(frame, 'Código :', 1, start_here = True)
    description = collector(frame, 'Descipción :', 2)
    cost        = collector(frame, 'Costo :', 3)
    price       = collector(frame, 'Precio :', 4)
    quantity    = collector(frame, 'Cantidad :', 5)

    # The list with the products
    headers_product = ['Código', 'Descripción', 'Costo', 'Precio', 'Cantidad']
    inventory_list = ttk.Treeview(frame, height = 15,
                                     columns = headers_product, show = 'headings')
    inventory_list.config(cursor = 'hand2')
    inventory_list.grid(row = 7, column = 0, columnspan = 4, 
                                            pady = 5, padx = 10, sticky = 'nse')

    # Assign scrollbar 
    scroll = ttk.Scrollbar(frame, orient = 'vertical', command = inventory_list.yview)
    scroll.grid(row = 7, column = 3, padx = 5, sticky = 'nse')
    inventory_list.configure(yscrollcommand = scroll.set)
    
    #### Set the heading
    for header in headers_product:
        inventory_list.heading(header, text = header)
    
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
        test_code  = len(code.value.get()) > 1 
        test_desc  = len(description.value.get()) > 1
                
        if test_code and test_desc:
            data.add_product(
                            str(code.value.get()), 
                            str(description.value.get()), 
                            float(cost.value.get()), 
                            float(price.value.get()), 
                            float(quantity.value.get())
                            )
        data.get_products(inventory_list)
        clean()

    def cancel_operation():
        labels_state(False)
        clean()

    # Buttons
    save_button   = button(frame, 'Crear', create_new_product, 'green_button', (6, 2))
    cancel_button = button(frame, 'Cancelar', cancel_operation, 'red_button', (6, 3))
    edit_button   = button(frame, 'Editar', 0, 'blue_button', (8,0))
    delete_button = button(frame, 'Eliminar', 0, 'black_button', (8,1))
    
    cancel_operation()
    root.mainloop()


if __name__ == '__main__':
    products()