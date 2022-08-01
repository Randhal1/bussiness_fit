import tkinter as tk
from turtle import width

def selection_menu(root): 
    main_menu = tk.Menu(root)
    root.config(menu = main_menu, width = 300, height = 300)

    # Menu creation 
    ## Start menu
    start_menu = tk.Menu(main_menu, tearoff = False)
    main_menu.add_cascade(label = 'Inicio', menu = start_menu)

    ### Items
    start_menu.add_command(label = 'Crear factura')
    start_menu.add_command(label = 'Cerrar sesión')
    start_menu.add_command(label = 'Salir', command = root.destroy)

    ## Personal menu
    personal_menu = tk.Menu(main_menu, tearoff = False)
    main_menu.add_cascade(label = 'Actividades', menu = personal_menu)
    personal_menu.add_command(label = 'Revisar inventario')
    personal_menu.add_command(label = 'Crear cliente')
    personal_menu.add_command(label = 'Crear producto')
    
    ## Ocasional events
    ocasional_menu = tk.Menu(main_menu, tearoff = False)
    main_menu.add_cascade(label = 'Finanzas', menu = ocasional_menu)
    ocasional_menu.add_command(label = 'Crear cobro')
    ocasional_menu.add_command(label = 'Crear pago')
    ocasional_menu.add_command(label = 'Crear copia de seguridad en excel')

    
class Frame(tk.Frame):
    # Inherit from class Frame in Tk module, set height
    def __init__(self, root):
        super().__init__(root, width = 800, height = 600)
        self.root = root
        self.pack()
    

if __name__ == '__main__':
    pass