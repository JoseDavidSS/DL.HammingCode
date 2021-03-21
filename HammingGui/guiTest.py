import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


# Set the app size
Window.size = (600,450) #(x,y) lengths

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1 # Set MyGridLayout columns
        self.row_force_default = True
        self.row_default_height = 150
        self.col_force_default = True
        self.col_default_width = 600

        # Create a second gridlayout
        self.topGrid = GridLayout(
            row_force_default = True,
            row_default_height = 50,
            col_force_default = True,
            col_default_width = 300)
        self.topGrid.cols = 2 # Set topGrid number of cols

        # Add Label and Input Box to topGrid
        self.topGrid.add_widget(Label(
            text="Name: ",
            font_size = 24))
        self.name = TextInput(
            multiline=False,
            font_size = 24)
        self.topGrid.add_widget(self.name)

        # Add Label and Input Box to topGrid
        self.topGrid.add_widget(Label(
            text="Pizza Favorita: ",
            font_size = 24))
        self.pizzaInput = TextInput(
            multiline=False,
            font_size = 24)
        self.topGrid.add_widget(self.pizzaInput)

        # Add Label and Input Box to topGrid
        self.topGrid.add_widget(Label(
            text="Color Favorito: ",
            font_size = 24))
        self.colorInput = TextInput(
            multiline=False,
            font_size = 24)
        self.topGrid.add_widget(self.colorInput)

        # Add the topGrid to MyGridLayout
        self.add_widget(self.topGrid)

        # Create a submit button
        self.submit = Button(
            text="Submit",
            font_size=32)
        self.submit.bind(on_press = self.press) #Bond function
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizzaInput.text
        color = self.colorInput.text

        #print(f'Hola {name}, you like {pizza} pizza, and your favorite color is {color}!')
        # Print in to the screen
        self.add_widget(Label(text=f'Hola {name}, you like {pizza} pizza, and your favorite color is {color}!'))

        # Clear inputs
        self.name.text = ""
        self.pizzaInput.text = ""
        self.colorInput.text = ""
        

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()
