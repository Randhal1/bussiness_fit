import tkinter as tk
from main_features.GUI_elements.styles import color

# This class creates the buttons
class button(tk.Button):
    def __init__(self, main_frame, button_text, button_command, style, location):
        super().__init__(main_frame, text = button_text, command = button_command)
        # Set style
        self.style = color(style)
        style_button = ('roboto', 12, 'bold')
        
        # Define command
        self.config(width = 15, font = style_button, fg = self.style['foreground'],
                        bg = self.style['background'], cursor = 'hand2', 
                        activebackground = self.style['active_bg'], bd = 0)

        # Set location
        self.grid(row = location[0], column = location[1], pady = 10)

    def button_color(self, changed):
        self.color = color(changed)
        self.config(fg = self.color['foreground'], bg = self.color['background'], 
                    activebackground = self.color['active_bg'])

if __name__ == '__main__':
    pass