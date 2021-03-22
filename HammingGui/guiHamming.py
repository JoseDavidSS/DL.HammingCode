import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window

from HammingGui import data
from HammingLogic import binConvertions
from graphGui import *
from tablesGui import *


# Set the app size
Window.size = (900,450) #(x,y) lengths


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1 # Set MyGridLayout columns
        self.row_force_default = True
        self.row_default_height = 75
        self.col_force_default = True
        self.col_default_width = 900

        #Create titel grid
        self.titelGrid = GridLayout(
            row_force_default = True,
            row_default_height = 75,
            col_force_default = True,
            col_default_width = 900)
        self.titelGrid.cols = 1
        
        self.titelGrid.add_widget(Label(text="Aplicación Hamming", font_size = 48))

        self.add_widget(self.titelGrid) # Add titelGrid to MyGridLayout


        # Division Label
        self.add_widget(Label(text="___________________________________________________________________________________________________________________________________________________________",
                              font_size = 16))

        #Create body grid
        self.bodyGrid = GridLayout(
            row_force_default = True,
            row_default_height = 30,
            col_force_default = True,
            col_default_width = 300)
        self.bodyGrid.cols = 3

        # First row
        self.bodyGrid.add_widget(Label(text="Ingrese su número binario:", font_size = 16))
        self.binaryNumber = TextInput(multiline=False, font_size = 16)
        self.bodyGrid.add_widget(self.binaryNumber)
        
        self.convertButton = Button(text="Convertir", font_size=16)
        self.convertButton.bind(on_press = self.press) #Bond function
        self.bodyGrid.add_widget(self.convertButton)

        # Second row
        self.decimalNumberLabel = Label(text="Su número en base decimal es:", font_size = 16)
        self.bodyGrid.add_widget(self.decimalNumberLabel)
        
        self.octalNumberLabel = Label(text="Su número en base octal es:", font_size = 16)
        self.bodyGrid.add_widget(self.octalNumberLabel)
        
        self.hexaNumberLabel = Label(text="Su número en base hexadecimal es:", font_size = 16)
        self.bodyGrid.add_widget(self.hexaNumberLabel)

        # Third row
        self.decimalNumberValue = Label(text="----------------------------------", font_size = 16)
        self.bodyGrid.add_widget(self.decimalNumberValue)
        
        self.octalNumberValue = Label(text="----------------------------------", font_size = 16)
        self.bodyGrid.add_widget(self.octalNumberValue)
        
        self.hexaNumberValue = Label(text="----------------------------------", font_size = 16)
        self.bodyGrid.add_widget(self.hexaNumberValue)
        
        # Add body grid to MyGridLayout
        self.add_widget(self.bodyGrid)

        # Division Label
        self.add_widget(Label(text="___________________________________________________________________________________________________________________________________________________________",
                              font_size = 16))

        #Create graphic grid
        self.graphicGrid = GridLayout(
            row_force_default = True,
            row_default_height = 30,
            col_force_default = True,
            col_default_width = 450)
        self.graphicGrid.cols = 2
        
        #Create graphic grid first row
        self.graphicGrid.add_widget(Label(text="Graficando código NZRI:", font_size = 16))
        self.graphingButton = Button(text="Graficar", font_size=16)
        self.graphingButton.bind(on_press = self.graphing) #Bond function
        self.graphicGrid.add_widget(self.graphingButton)

        # Division Label
        self.graphicGrid.add_widget(Label(text="___________________________________________________________________________________________________________________________________________________________",
                              font_size = 16))
        self.graphicGrid.add_widget(Label(text="___________________________________________________________________________________________________________________________________________________________",
                              font_size = 16))

        #Create graphic grid second row
        self.graphicGrid.add_widget(Label(text="Código Hamming:", font_size = 16))
        self.tabulateButton = Button(text="Tabular", font_size=16)
        self.tabulateButton.bind(on_press=self.tabs)  # Bond function
        self.graphicGrid.add_widget(self.tabulateButton)

        self.add_widget(self.graphicGrid) # Add graphicGrid to MyGridLayout

        # Division Label
        self.graphicGrid.add_widget(Label(text="___________________________________________________________________________________________________________________________________________________________",
                              font_size = 16))
        self.graphicGrid.add_widget(Label(text="___________________________________________________________________________________________________________________________________________________________",
                              font_size = 16))


        
    # Converting method   
    def press(self, instance):

        binNum = self.binaryNumber.text # tipo de dato string

        for i in binNum:
            if int(i) == 0 or int(i)==1:
                pass
            else:
                return False
        self.decimalNumberValue.text = binConvertions.bin2dec(binNum)  # convertirDecimal(binNum)
        self.octalNumberValue.text = binConvertions.bin2oct(binNum)  # convertirOctal(binNum)
        self.hexaNumberValue.text = binConvertions.bin2hex(binNum)  # convertirHexadecimal(binNum)

    # Graphing method
    def graphing(self, instance):
        data.graficoActivo = 1
        MyApp().stop()
        #self.add_widget(prueba.IngresarNumero())

    # Creating tabs
    def tabs(self, instance):
        data.graficoActivo = 2
        MyApp().stop()

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        print(data.graficoActivo)
        if data.graficoActivo == 0:
            return MyGridLayout()
        elif data.graficoActivo == 1:
            return IngresarNumero()
        else:
            return tablesGrid()

if __name__ == '__main__':
    MyApp().run()

MyApp().run()

data.graficoActivo = 0
print(data.graficoActivo)

MyApp().run()

if __name__ == '__main__':
    MyApp().run()











