import tkinter as tk

# Creates desplegable menus
class selection_menu:
    
    # Set desplegable menu titles
    def __init__(self, root_menu, title, dict_of_labels):
        
        self.menu = tk.Menu(root_menu, tearoff = False)
        root_menu.add_cascade(label = title, menu = self.menu)

        for labels, command in dict_of_labels.items():
            self.Labels(labels, command)

    # set desplegable menus items    
    def Labels(self, item, this_command):
        self.menu.add_command(label = item, command = this_command)   


if __name__ == '__main__':
    pass