import guizero as gui
import dateoperations as dateops
import apioperations as apiops
import webbrowser

# App -----

app = gui.App(title='Pixela Habit Tracker', layout='grid', width=510, height=340)
app.bg = '#FFFAFA'


# Functions -----


def submit_request_to_api():
    """Primary app function."""
    username = username_entry_textbox.value
    graph_id = graph_name_combo.value
    request_type = pixel_options.value
    date_choice = date_option.value
    custom_date = date_entry_textbox.value
    quantity = quantity_entry_textbox.value

    submit_request_with_values(username, graph_id, request_type, date_choice, custom_date, quantity)


def submit_request_with_values(username, graph_id, request_type, date_choice, custom_date, quantity):
    """Receives values from the GUI, processes for errors, and calls the appropriate API."""
    dateops_response = dateops.date_handler(date_choice, custom_date)
    if dateops_response == 'invalid date':
        app.error(title='Invalid Date', text='You entered an invalid date.\n'
                                             'Please try again.')
    elif dateops_response == 'date out of range':
        app.error(title='Date Out Of Range', text='The date you entered is in the future or too far in the past.\n'
                                                  'Please try again.')
    else:
        date_for_api = dateops_response

        if request_type == 'delete':
            delete_pixel_response = apiops.delete_existing_pixel(username, graph_id, date_for_api)
            check_api_response(delete_pixel_response)
        else:
            if not is_quantity_greater_than_zero(quantity):
                app.error(title='Quantity Too Low', text='The quantity should be a positive integer or decimal.\n'
                                                         'Please try again.')
            else:
                if request_type == 'add':
                    post_pixel_response = apiops.post_new_pixel(username, graph_id, date_for_api, quantity)
                    check_api_response(post_pixel_response)
                elif request_type == 'modify':
                    put_pixel_response = apiops.put_pixel_modification(username, graph_id, date_for_api, quantity)
                    check_api_response(put_pixel_response)


def is_quantity_greater_than_zero(quantity):
    """Checks if quantity is greater than zero and returns a Boolean."""
    true_or_false = True
    if quantity == '' or float(quantity) <= 0:
        true_or_false = False
    return true_or_false


def check_api_response(response):
    """Checks the API response, indicates success and clears the app, or creates an error pop-up."""
    if response[0]:
        success_error_image.image = 'images/success.png'
        app.after(4000, reset_app)
    else:
        app.error(title='API Error', text=f'Oops! Something went wrong:\n{response[1]}')


def reset_app():
    """Clears text entry boxes and resets radio button selections."""
    quantity_entry_textbox.clear()
    date_entry_textbox.clear()
    success_error_image.image = 'images/blank.png'
    pixel_option_button_list = pixel_options.children
    pixel_option_button_list[0].tk.select()
    date_option_button_list = date_option.children
    date_option_button_list[0].tk.select()
    quantity_entry_textbox.focus()


def open_graph_url():
    """Opens the selected graph in a browser window."""
    username = username_entry_textbox.value
    graph_name = graph_name_combo.value
    graph_url = f'https://pixe.la/v1/users/{username}/graphs/{graph_name}.html'
    webbrowser.open_new(graph_url)


def change_to_custom():
    """Changes the date option radio button selection to 'custom.'"""
    date_option_button_list = date_option.children
    date_option_button_list[1].tk.select()


# Widgets -----

# # Header Box
header_box = gui.Box(app, grid=[0, 0, 3, 1], width=510, height=80)

header_sub_box = gui.Box(header_box)
pixela_logo = gui.Picture(header_sub_box, image='images/PIXELA_RED.png', width=60, height=60, align='left')
header_text = gui.Text(header_sub_box, text='Habit Tracker', align='right', size=48)

# # Graph Properties Box
graph_properties_box = gui.Box(app, grid=[0, 1, 3, 1], width=510, height=60, layout='grid')

username_box = gui.Box(graph_properties_box, grid=[0, 0], width=150, height=60)
username_text = gui.Text(username_box, text='Username: ', size=11, color='red', align='left')
username_entry_textbox = gui.TextBox(username_box, text='aeversme', width=11, align='right')

graph_button_box = gui.Box(graph_properties_box, grid=[1, 0], width=160, height=60)
graph_button_box.tk.config(pady=15)
graph_button = gui.PushButton(graph_button_box, open_graph_url, text='Go to my graph!', pady=5)

graph_id_box = gui.Box(graph_properties_box, grid=[2, 0], width=150, height=60)
graph_id_text = gui.Text(graph_id_box, text='Graph ID: ', size=11, color='red', align='left')
graph_name_combo = gui.Combo(graph_id_box,
                             options=[
                                 'graph1',
                                 'test1'
                             ],
                             selected='graph1',
                             width=11,
                             align='right')

# # Pixel Options Box
pixel_options_box = gui.Box(app, grid=[0, 2], width=170, height=140)

pixel_options_box_heading = gui.Text(pixel_options_box, text='Pixel Options:', size=11, color='red')
pixel_options_box_heading.tk.config(pady=12)
pixel_options = gui.ButtonGroup(pixel_options_box,
                                options=[['Add a pixel', 'add'],
                                         ['Modify a pixel', 'modify'],
                                         ['Delete a pixel', 'delete']],
                                selected='add')

# # Date Options Box
date_options_box = gui.Box(app, grid=[1, 2], width=170, height=140)

date_options_box_heading = gui.Text(date_options_box, text='Date options:', size=11, color='red')
date_options_box_heading.tk.config(pady=12)
date_option = gui.ButtonGroup(date_options_box,
                              options=[['Today', 'today'],
                                       ['Custom:', 'custom']],
                              selected='today')
date_entry_textbox = gui.TextBox(date_options_box, text='', width=12)
date_entry_textbox.when_clicked = change_to_custom
date_hint_text = gui.Text(date_options_box, text='(YYYY-M-D)', size=8)

# Quantity Box
quantity_box = gui.Box(app, grid=[2, 2], width=170, height=140)

quantity_box_heading = gui.Text(quantity_box, text='Pixel Quantity:', size=11, color='red')
quantity_box_heading.tk.config(pady=12)
quantity_entry_textbox = gui.TextBox(quantity_box, text='', width=5)
quantity_entry_textbox.focus()
success_error_image = gui.Picture(quantity_box, image='images/blank.png')
success_error_image.tk.config(pady=20)

# Button Box
button_box = gui.Box(app, grid=[0, 3, 3, 1], width=510, height=60)

button_sub_box = gui.Box(button_box, width=250, height=60)
button_sub_box.tk.config(pady=10)
submit_button = gui.PushButton(button_sub_box, submit_request_to_api, text='Submit', align='left', pady=5, width=6)
reset_button = gui.PushButton(button_sub_box, reset_app, text='Reset', align='right', pady=5, width=6)


# Display -----

app.display()
