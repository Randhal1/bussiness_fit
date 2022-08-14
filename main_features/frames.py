from start_module import run
run()

import tkinter as tk
from tkinter import HORIZONTAL, ttk
from main_features.GUI_elements.selection_menu import selection_menu
from PIL import ImageTk, Image


class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width = 800, height = 600)
        self.root = root
        self.root.config(background = '#fcfcfc')
        # Define window title and icon 
        self.root.title('Inventory: Software punto de ventas')
        self.root.iconbitmap('branx_sources/main_ico.ico')
        
        #self.menus()
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

    def read_image(self, path, size):
        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

    def image_frame(self, loc, source, bckg, size = (200, 200)):
        logo_image = self.read_image(source, size)
        logo       = tk.Label(self, image = logo_image, bg = bckg)
        logo.image = logo_image

        logo.grid(row = loc[0], column = loc[1])

    def row_space(self, distance, column, bckg):
        for row in distance:
            tk.Label(self, text = '', bg = bckg).grid(row = row, column = column)

    def single_row_space(self, row, column, bckg):
        tk.Label(self, text ='', bg = bckg).grid(row = row, column = column)

    def center_window(self, app_width, app_height):
        x_width = self.winfo_screenwidth()
        y_width = self.winfo_screenheight()
        x = int((x_width - app_width)/2)
        y = int((y_width - app_height)/2)

        return self.root.geometry(f'{app_width}x{app_height}+{x}+{y}')

if __name__ == '__main__':
    root  = tk.Tk()
    frame = Frame(root)
    frame.center_window(300, 300)
    root.mainloop()