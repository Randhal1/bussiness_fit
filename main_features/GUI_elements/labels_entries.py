import tkinter as tk

# This class define the label, value and input of elements
class collector:
    def __init__(self, main_frame, field_name, location, start_here = False):

        # Style of text
        style_labels = ('roboto', 12, 'bold')
        style_entry  = ('roboto', 12, 'bold')

        # define value field
        self.value = tk.StringVar()
        
        # define the label
        self.label = tk.Label(main_frame, text = field_name, font = style_labels)
        self.label.grid(row = location, column = 1, sticky = tk.E)
        
        # define entry
        self.field_entry = tk.Entry(main_frame, textvariable = self.value)
        if start_here:
            self.field_entry.focus()
        self.field_entry.config(width = 50, font = style_entry)
        self.field_entry.grid(row = location, column = 2, padx = 10, pady = 5, columnspan = 2)

if __name__ == '__main__':
    pass