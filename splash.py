from math import prod
from main_features.start_module import run
run

import tkinter as tk
from inventory import products
from people import people
from main_features.frames import Frame
from main_features.GUI_elements.buttons import button

def main(root, user, passwd):
    
    frame_color = '#C30015'
    frame       = Frame(root)
    frame.config(background = frame_color)
    frame.center_window(700, 420)
    
    root.resizable(False, False)

    # Buttons functions
    def inventory_callback():
        inv_frame = tk.Toplevel(root)
        products(inv_frame, user, passwd)

    def people_callback():
        inv_frame = tk.Toplevel(root)
        people(inv_frame, user, passwd)

    def invoice_callback():
        pass

    # Inventory
    frame.single_row_space(0, 0,frame_color) 
    inventory_img = frame.image_frame((1,0), './branx_sources/inventory.png', frame_color)
    frame.row_space(range(2, 9), 0, frame_color)
    inv_button = button(frame, 'Inventario', inventory_callback, 'blue_button', (10,0))
    inv_button.grid(padx = 40)

    # People
    frame.single_row_space(0, 1,frame_color)
    people_img = frame.image_frame((1,1), './branx_sources/people.png', frame_color)
    frame.row_space(range(2, 9), 1, frame_color)
    ppl_button = button(frame, 'Clientes', people_callback, 'green_button', (10,1))
    ppl_button.grid(padx = 40)

    # Invoices
    frame.single_row_space(0, 2,frame_color)
    invoice_img = frame.image_frame((1,2), './branx_sources/invoice.png', frame_color)
    frame.row_space(range(2, 9), 2, frame_color)
    chkin_button = button(frame, 'Facturas', invoice_callback, 'black_button', (10,2))
    chkin_button.grid(padx = 40)

if __name__ == '__main__':
    pass