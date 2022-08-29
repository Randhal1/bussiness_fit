import tkinter as tk

# This class define the label, value and input of elements
class collector:
    def __init__(self, main_frame, field_name, location, 
                    displace = 0, start_here = False):

        # Style of text
        style_labels = ('verdana', 12, 'bold')
        style_entry  = ('verdana', 12, 'bold')

        # define value field
        self.value = tk.StringVar()
        
        # define the label
        self.label = tk.Label(main_frame, text = field_name, font = style_labels)
        self.label.grid(row = location, column = 1 + displace, sticky = tk.E)
        self.label.config(background = '#fcfcfc')
        
        # define entry
        self.field_entry = tk.Entry(main_frame, textvariable = self.value)
        if start_here:
            self.field_entry.focus()
        self.field_entry.config(width = 50, font = style_entry, background = '#D4E6F1')
        self.field_entry.grid(row = location, column = 2 + displace, 
                                padx = 10, pady = 5, columnspan = 2)

if __name__ == '__main__':
    pass