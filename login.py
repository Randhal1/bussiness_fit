from main_features.start_module import run
run()

import tkinter as tk
from tkinter import messagebox
from main_features.frames import Frame
from main_features.GUI_elements.labels_entries import collector
from main_features.GUI_elements.buttons import button
from splash import main

def login_screen(root):
    root.iconify()
    login_root = tk.Toplevel(root)
    login_root.resizable(False, False)
    # Styles and info app
    style_labels = ('verdana', 10, 'bold')
    name = 'Inventory: Sales'
    version = 'Alpha 0.1'

    # Left frame
    frame_logo = Frame(login_root)
    frame_logo.center_window(600, 300)
    #frame_logo.image_frame((0, 0), './branx_sources/dmd-doc-icon.png', '#5D6D7E')
    frame_logo.config(bd = 0, width = 200, height = 300, relief = tk.SOLID, 
                    bg = '#5D6D7E', padx = 30, pady = 10)
    frame_logo.pack(side = 'left', expand = tk.YES, fill = tk.BOTH)

    logo  = frame_logo.read_image('./branx_sources/dmd-doc-icon.png', (130, 130))

    label = tk.Label(frame_logo, image = logo, bg = '#5D6D7E')
    label.image = logo
    label.place(x = 0, y = 0, relheight = 1, relwidth = 1)

    # Right frame
    frame_data = Frame(login_root)
    frame_data.config(bd=0, relief=tk.SOLID, bg='#fcfcfc')

    user_name_field = collector(frame_data, 'Usuario: ', 3, start_here = True)
    user_name_field.field_entry.config(width = 20)
    passwd_field  = collector(frame_data, 'Contraseña:', 4)
    passwd_field.field_entry.config(show = '●', width = 20)

    frame_data.pack(side='right', expand=tk.YES, fill=tk.BOTH)

    label_logo = tk.Label(frame_data, text= f'{name} \n {version}', font = style_labels,
                        fg="#666a88", bg='#fcfcfc', pady=50)
    label_logo.grid(row = 1, column = 2)
    
    def login():
        user   = user_name_field.value.get()
        passwd = passwd_field.value.get()

        try:
            login_root.destroy()
            main(root, user, passwd)
            root.deiconify()
        except:
            messagebox.showerror('Ejecucion fallida',
                'No se puede conectar a DB001')

    
    login_btn = button(frame_data, 'Iniciar sesión', login, 'purple_button', (5, 2))

    login_root.bind('<Return>', lambda event: login())

if __name__ == '__main__':
    root = tk.Tk()
    login_screen(root)
    root.mainloop()