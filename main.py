import guizero as gui

# App -----
app = gui.App(title='Pixela Habit Tracker')
app.bg = '#FFFAFA'

# Functions -----


def do_something():
    changing_text.value = graph_name_text_box.value
    pixel_choice.value = pixel_action.value_text
    success_error_image.image = 'images/success.png'


def reset():
    quantity_text_box.clear()
    graph_name_text_box.value = 'graph1'
    dd.value = 'dd'
    mm.value = 'mm'
    yyyy.value = 'yyyy'


# Widgets -----
pixela_logo = gui.Picture(app, image='images/PIXELA_RED.png', width=60, height=60)
banner_text = gui.Text(app, text='Habit Tracker')
banner_text.text_size = 40

graph_name_text = gui.Text(app, text='Graph name:')

graph_name_text_box = gui.TextBox(app, 'graph1', width=10)

submit_button = gui.PushButton(app, do_something, text='Submit')
reset_button = gui.PushButton(app, reset, text='Reset')

changing_text = gui.Text(app, text='')

pixel_action = gui.ButtonGroup(app,
                               options=[
                                   ['Add a pixel', 'add'],
                                   ['Modify a pixel', 'modify'],
                                   ['Delete a pixel', 'delete']
                               ],
                               horizontal='False',
                               selected='add')

pixel_choice = gui.Text(app, text='')

day_selection = gui.ButtonGroup(app,
                                options=[
                                    ['Today', 'today'],
                                    ['Another day', 'other day']
                                ],
                                horizontal='False',
                                selected='today')

dd = gui.TextBox(app, text='dd', width=4)
mm = gui.TextBox(app, text='mm', width=4)
yyyy = gui.TextBox(app, text='yyyy', width=4)

quantity_text = gui.Text(app, text='Quantity: ')
quantity_text_box = gui.TextBox(app, text='', width=4)

success_error_image = gui.Picture(app, image='images/blank.png')

# Display -----
app.display()
