import guizero as gui

# App -----
app = gui.App(title='Pixela Habit Tracker')
app.bg = '#FFFAFA'

# Functions -----


def do_something():
    changing_text.value = text_box.value
    pixel_choice.value = pixel_action.value


# Widgets -----
pixela_logo = gui.Picture(app, image='images/PIXELA_RED.png', width=60, height=60)
banner_text = gui.Text(app, text='Habit Tracker')
banner_text.text_size = 40

instructions = gui.Text(app, text='Type something in the box and then push the button.')

text_box = gui.TextBox(app, '', width=20)

button = gui.PushButton(app, do_something, text='PUSH ME')
button.bg = 'red'
button.text_color = 'white'

changing_text = gui.Text(app, text='')

pixel_action = gui.ButtonGroup(app, options=['Add a pixel', 'Modify a pixel', 'Delete a pixel'], selected='Add a pixel')

pixel_choice = gui.Text(app, text='')

# Display -----
app.display()
