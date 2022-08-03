# Define ibject color

colors = {
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
    }
}

def color(color_name):
    color_style = colors[color_name]
    return color_style

if __name__ == '__main__':
    print(color('blue_button'))