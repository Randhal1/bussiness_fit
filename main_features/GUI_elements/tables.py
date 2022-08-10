from tkinter import ttk
from tkinter import *
from styles import color as color_style

class Table(ttk.Treeview):
    
    def __init__(self, frame, headers, row_loc, colums_len, scroll_col,
                color, rows_qty = 15):
        super().__init__(frame, height = rows_qty,
                        columns = headers, show = 'headings')

        header_style = ('roboto', 12, 'bold')
        body_style = ('Cascadia Mono', 11, 'bold')
        table_style = ttk.Style()
        table_style.configure("Treeview.Heading", font = header_style)
        table_style.configure("Treeview", highlightthickness = 0, bd = 0, font = body_style)

        self.config(cursor = 'hand2')
        self.grid(row = row_loc, column = 0, columnspan = colums_len, 
                                                pady = 5, padx = 35, sticky = 'nse')

        

        # Assign scrollbar 
        scroll = ttk.Scrollbar(frame, orient = 'vertical', command = self.yview)
        scroll.grid(row = row_loc, column = scroll_col, padx = 5, sticky = 'nse')
        self.configure(yscrollcommand = scroll.set)
        
        #### Set the heading
        for header in headers:
            self.heading(header, text = header)

        self.tag_configure('odd', background  = color_style(color)['odd'])
        self.tag_configure('even', background = color_style(color)['even'])


if __name__ == '__main__':
    pass