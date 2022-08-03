import tkinter as tk
from main_features.GUI_elements.selection_menu import selection_menu

class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width = 800, height = 600)
        self.root = root
        self.menus()
        self.pack()
        
    def menus(self): 
        main_menu = tk.Menu(self.root)
        self.root.config(menu = main_menu, width = 300, height = 300)

        # Menu creation 
        start_menu_items = {
            'Crear factura'     : 0,
            'Crear cliente'     : 0,
            'Listar inventario' : 0, 
            'Salir'             : self.root.destroy
        }
        start_menu = selection_menu(main_menu, 'Inicio', start_menu_items)

        login_menu_items = {
            'Ver sesion'    : 0,
            'Ver facturas'  : 0,
            'Ver clientes'  : 0,
            'Cerrar sesion' : 0
        }
        login_menu = selection_menu(main_menu, 'Actividades', login_menu_items)
        
        finance_menu_items = {
            'Crear cobro'   :  0,
            'Crear pago'    :  0,
            'Backup excel'  : 0
        }
        finance_menu = selection_menu(main_menu, 'Creditos', finance_menu_items)

if __name__ == '__main__':
    root  = tk.Tk()
    frame = Frame(root) 
    root.mainloop()