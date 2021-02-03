import guizero as gui

app = gui.App(title='Pixela Habit Tracker')
app.bg = '#FFFAFA'
pixela_logo = gui.Picture(app, image='images/PIXELA_RED.png', width=60, height=60)
welcome_message = gui.Text(app, text='Habit Tracker')
welcome_message.text_size = 40
app.display()
