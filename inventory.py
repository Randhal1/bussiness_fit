import tkinter as tk
from tkinter import ttk
from main_features.frames import Frame, selection_menu
from main_features.dbconections import DB_conection

root = tk.Tk()
data = DB_conection()

def products():

    # Create frame
    frame = Frame(root)
    ## Input labels

    style_labels = ('roboto', 12, 'bold')
    style_entry  = ('roboto', 12, 'bold')
    style_button = ('roboto', 12, 'bold')
    style_table  = ('roboto', 12, 'bold')
    
    ### Code label
    value_code = tk.StringVar()
    label_code = tk.Label(frame, text = 'Código: ', font = style_labels)
    label_code.grid(row = 1, column = 1, sticky = tk.E)
    code = tk.Entry(frame, textvariable = value_code)
    code.focus()
    code.config(width = 50, font = style_entry)
    code.grid(row = 1, column = 2, padx = 10, pady = 5, columnspan = 2)

    ### Description label
    value_description = tk.StringVar()
    label_description = tk.Label(frame, text = 'Descripción: ', font = style_labels)
    label_description.grid(row = 2, column = 1, sticky = tk.E)
    description = tk.Entry(frame, textvariable = value_description)
    description.config(width = 50, font = style_entry)
    description.grid(row = 2, column = 2, padx = 10, pady = 5, columnspan = 2)

    ### Cost label
    value_cost = tk.StringVar()
    cost_label= tk.Label(frame, text = 'Costo: ', font = style_labels)
    cost_label.grid(row = 3, column = 1, sticky = tk.E)
    cost = tk.Entry(frame, textvariable = value_cost)
    cost.config(width = 50, font = style_entry)
    cost.grid(row = 3, column = 2, padx = 10, pady = 5, columnspan = 2)

    ### Price label
    value_price = tk.StringVar()
    price_label = tk.Label(frame, text = 'Precio: ', font = style_labels)
    price_label.grid(row = 4, column = 1, sticky = tk.E)
    price = tk.Entry(frame, textvariable = value_price)
    price.config(width = 50, font = style_entry)
    price.grid(row = 4, column = 2, padx = 10, pady = 5, columnspan = 2)

    ### Quantity label
    value_quantity = tk.StringVar()
    qty_label = tk.Label(frame, text = 'Cantidad: ', font = style_labels)
    qty_label.grid(row = 5, column = 1, sticky = tk.E)
    quantity = tk.Entry(frame, textvariable = value_quantity)
    quantity.config(width = 50, font = style_entry)
    quantity.grid(row = 5, column = 2, padx = 10, pady = 5, columnspan = 2)

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

    # Buttons section for product

    ## Define buttons operations
    ### An auxiliar function
    def clean():
        value_code.set('')
        value_description.set('')
        value_cost.set('')
        value_price.set('')
        value_quantity.set('')

    def create_new_product(): # Also add new line
        save_button['text'] = 'Guardar'
        code.config(state = 'normal')
        description.config(state = 'normal')
        cost.config(state = 'normal')
        price.config(state = 'normal')
        quantity.config(state = 'normal')
        cancel_button.config(state = 'normal')
        
        test_code  = len(value_code.get()) > 1 
        test_desc  = len(value_description.get()) > 1
                
        if test_code and test_desc:
            data.add_product(
                            str(value_code.get()), 
                            str(value_description.get()), 
                            float(value_cost.get()), 
                            float(value_price.get()), 
                            float(value_quantity.get())
                            )
        
        data.get_products(inventory_list)
        clean()

    def cancel_operation():
        save_button['text'] = 'Crear'
        code.config(state = 'disabled')
        description.config(state = 'disabled')
        cost.config(state = 'disabled')
        price.config(state = 'disabled')
        quantity.config(state = 'disabled')
        cancel_button.config(state = 'disabled')
        clean()

    # Save button
    save_button = tk.Button(frame, text = 'Crear', command = create_new_product)
    save_button.config(width = 15, font = style_button, fg = '#f0f8ff', bg = '#008b45',
                    cursor = 'hand2', activebackground = '#458b74')
    save_button.grid(row = 6, column = 2, pady = 10)
    
    # Cancel button
    cancel_button = tk.Button(frame, text = 'Cancelar', command = cancel_operation) 
    cancel_button.config(width = 15, font = style_button, fg = '#f0f8ff', bg = '#ee3b3b',
                    cursor = 'hand2', activebackground = '#a52a2a')
    cancel_button.grid(row = 6, column = 3, pady = 10)

    def guano():
        try:
            print(inventory_list.item(inventory_list.selection())['values'][0])
        except IndexError:
            pass

    # Edit button
    edit_button = tk.Button(frame, text = 'Editar', command = guano) 
    edit_button.config(width = 15, font = style_button, fg = '#F2F0A1', bg = '#0085CA',
                    cursor = 'hand2', activebackground = '#74D1EA')
    edit_button.grid(row = 8, column = 0, pady = 5)

    # Delete button
    delete_button = tk.Button(frame, text = 'Eliminar') 
    delete_button.config(width = 15, font = style_button, fg = '#ffffff', bg = '#1D252D',
                    cursor = 'hand2', activebackground = '#74D1EA')
    delete_button.grid(row = 8, column = 1, pady = 5)

    cancel_operation()


def run():
    # Set program icon, title and properties
    root.title('Inventory: Software punto de ventas')
    root.iconbitmap('branx_sources/main_ico.ico')
    root.resizable(1,1) # (x,y) resize, 1 = True, 0 = False

    # Create menu 
    selection_menu(root)
    
    # View products fields
    products()
    
    root.mainloop()


if __name__ == '__main__':
    run()