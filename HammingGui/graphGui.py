
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

from HammingGui import guiHamming


class IngresarNumero(GridLayout):
    def __init__(self, **kwargs):
        super(IngresarNumero, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Código NZRI', size_hint=(0.2, 0.1), pos=(0, 0)))
        self.row_force_default = True
        self.row_default_height = 30

        #Create graphBody grid
        self.graphBody = GridLayout(
            row_force_default = True,
            row_default_height = 30,
            col_force_default = True,
            col_default_width = 300)

        self.graphBody.cols = 3
        self.graphBody.add_widget(Label(text='Ingrese su número binario:', size_hint=(0.2, 0.1), pos=(0, 0)))
        self.binaryNumberGraph = TextInput(multiline=False, font_size = 16)
        self.graphBody.add_widget(self.binaryNumberGraph)

        self.refrescarBoton = Button(text="Analizar")
        self.refrescarBoton.bind(on_press=self.press)
        self.graphBody.add_widget(self.refrescarBoton)

        self.add_widget(self.graphBody)

        #Create plot grid
        self.plotGrid = GridLayout(
            row_force_default = True,
            row_default_height = 300,
            col_force_default = True,
            col_default_width = 900)
        self.plotGrid.cols = 1

        x = 0
        y = 0
        plt.step(x, y)
        self.plot = FigureCanvasKivyAgg(plt.gcf())
        self.plotGrid.add_widget(self.plot)

        self.add_widget(self.plotGrid)

        #Create volver grid
        self.volverGrid = GridLayout(
            row_force_default = True,
            row_default_height = 30,
            col_force_default = True,
            col_default_width = 300)
        self.volverGrid.cols = 1

        self.volver = Button(text="Volver",
                             size_hint_y = None,
                             height = 30,
                             size_hint_x = None,
                             width = 300)
        self.volver.bind(on_press=self.volverPrincipal)
        self.volverGrid.add_widget(self.volver)

        self.plotGrid.add_widget(self.volverGrid)

    def press(self, instance):
        print("entré")
        plt.clf()
        self.plotGrid.remove_widget(self.plot)
        self.plotGrid.remove_widget(self.volverGrid)
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        y = self.binaryNumberGraph.text
        print("dato y:")
        print(y)
        y = [int(x) for x in y]
        plt.step(x, y)
        plt.xticks(x)
        plt.yticks([0, 1])
        self.plot = FigureCanvasKivyAgg(plt.gcf())
        self.plotGrid.add_widget(self.plot)
        self.plotGrid.add_widget(self.volverGrid)


    def volverPrincipal(self, instance):

        #print(data.graficoActivo)
        print("hola")
        guiHamming.MyApp().stop()



class GraphApp(App):
    def build(self):
        return IngresarNumero()


if __name__ == '__main__':
    GraphApp().run()


