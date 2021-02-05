import guizero as gui

# App -----
app = gui.App(title='Pixela Habit Tracker', layout='grid', width=510, height=340)
app.bg = '#FFFAFA'

# Functions -----


def do_something():
    # changing_text.value = graph_name_text_box.value
    # pixel_choice.value = pixel_action.value_text
    # success_error_image.image = 'images/success.png'
    pass


def reset():
    # quantity_text_box.clear()
    # graph_name_text_box.value = 'graph1'
    # dd.value = 'dd'
    # mm.value = 'mm'
    # yyyy.value = 'yyyy'
    pass


def open_graph_url():
    pass


# Widgets -----

# # Header Box
header_box = gui.Box(app, grid=[0, 0, 3, 1], width=510, height=70)

header_sub_box = gui.Box(header_box)
pixela_logo = gui.Picture(header_sub_box, image='images/PIXELA_RED.png', width=60, height=60, align='left')
header_text = gui.Text(header_sub_box, text='Habit Tracker', align='right', size=40)

# # Graph Properties Box
graph_properties_box = gui.Box(app, grid=[0, 1, 3, 1], width=510, height=60, layout='grid')

username_box = gui.Box(graph_properties_box, grid=[0, 0], width=150, height=60)
username_text = gui.Text(username_box, text='Username: ', size=11, color='red', align='left')
username_textbox = gui.TextBox(username_box, text='aeversme', width=11, align='right')

graph_button_box = gui.Box(graph_properties_box, grid=[1, 0], width=160, height=60)
graph_button_box.tk.config(pady=10)
graph_button = gui.PushButton(graph_button_box, open_graph_url, text='Go to my graph!')

graph_id_box = gui.Box(graph_properties_box, grid=[2, 0], width=150, height=60)
graph_id_text = gui.Text(graph_id_box, text='Graph ID: ', size=11, color='red', align='left')
graph_id_textbox = gui.TextBox(graph_id_box, text='graph1', width=11, align='right')

# # Pixel Options Box
pixel_options_box = gui.Box(app, grid=[0, 2], width=170, height=150)

pixel_options_box_text = gui.Text(pixel_options_box, text='Pixel Options:', size=11, color='red')
pixel_options_box_text.tk.config(pady=12)
pixel_options = gui.ButtonGroup(pixel_options_box,
                                options=[['Add a pixel', 'add'],
                                         ['Modify a pixel', 'modify'],
                                         ['Delete a pixel', 'delete']],
                                selected='add')

# # Date Options Box
date_options_box = gui.Box(app, grid=[1, 2], width=170, height=150)

date_options_box_text = gui.Text(date_options_box, text='Date options:', size=11, color='red')
date_options_box_text.tk.config(pady=12)
date_options = gui.ButtonGroup(date_options_box,
                               options=[['Today', 'today'],
                                        ['Custom:', 'custom']],
                               selected='today')
date_entry = gui.TextBox(date_options_box, text='', width=12)
date_hint_text = gui.Text(date_options_box, text='(YYYY-MM-DD)', size=8)

# Quantity Box
quantity_box = gui.Box(app, grid=[2, 2], width=170, height=150)

quantity_box_text = gui.Text(quantity_box, text='Pixel Quantity:', size=11, color='red')
quantity_box_text.tk.config(pady=12)
quantity_entry_box = gui.TextBox(quantity_box, text='', width=5)
success_error_image = gui.Picture(quantity_box, image='images/blank.png')
success_error_image.tk.config(pady=20)

# Button Box
button_box = gui.Box(app, grid=[0, 3, 3, 1], width=510, height=60)

button_sub_box = gui.Box(button_box, width=200, height=60)
button_sub_box.tk.config(pady=10)
submit_button = gui.PushButton(button_sub_box, do_something, text='Submit', align='left')
reset_button = gui.PushButton(button_sub_box, reset, text='Reset', align='right')

# Display -----
app.display()
