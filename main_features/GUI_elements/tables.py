from tkinter import ttk
from tkinter import *

class Table(ttk.Treeview):
    
    def __init__(self, frame, headers_colums_names):
        super().__init__(frame, height = 15,
                        columns = headers_colums_names, show = 'headings')

        header_style = ('roboto', 12, 'bold')
        body_style = ('Cascadia Mono', 11, 'bold')
        table_style = ttk.Style()
        table_style.configure("Treeview.Heading", font = header_style)
        table_style.configure("Treeview", highlightthickness = 0, bd = 0, font = body_style)

        self.config(cursor = 'hand2')
        self.grid(row = 7, column = 0, columnspan = 4, 
                                                pady = 5, padx = 35, sticky = 'nse')

        

        # Assign scrollbar 
        scroll = ttk.Scrollbar(frame, orient = 'vertical', command = self.yview)
        scroll.grid(row = 7, column = 3, padx = 5, sticky = 'nse')
        self.configure(yscrollcommand = scroll.set)
        
        #### Set the heading
        for header in headers_colums_names:
            self.heading(header, text = header)

        self.tag_configure('odd', background  = '#ebf6ff')
        self.tag_configure('even', background = '#fffcfc')


if __name__ == '__main__':
    pass