# Define ibject color

colors = {

    # Buttons colors

    'green_button': {
        'background': '#008b45',
        'foreground': '#f0f8ff',
        'active_bg' : '#458b74'
    },
    'red_button': {
        'background': '#ee3b3b',
        'foreground': '#f0f8ff',
        'active_bg' : '#a52a2a'
    },
    'blue_button': {
        'background': '#0085CA',
        'foreground': '#F2F0A1',
        'active_bg' : '#74D1EA'
    },
    'black_button': {
        'background': '#1D252D',
        'foreground': '#ffffff',
        'active_bg' : '#74D1EA'
    },
    'orange_button': {
        'background': '#FF5733',
        'foreground': '#FDE9E4',
        'active_bg' : '#BE2200'
    },
    'purple_button': {
        'background': '#4A0084',
        'foreground': '#E2E2E2',
        'active_bg' : '#B454FF'
    },

    # Tables colors

    'blue_table': {
        'odd' : '#fffcfc',
        'even': '#ebf6ff'
    },
    'red_table': {
        'odd' : '#FFB5B5',
        'even': '#FFF4F4'
    },
    'green_table': {
        'odd' : '#A4FFC2',
        'even': '#EFFFF4'
    }
}

def color(color_name):
    color_style = colors[color_name]
    return color_style

if __name__ == '__main__':
    pass