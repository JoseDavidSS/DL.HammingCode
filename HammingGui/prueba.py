from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen


class IngresarNumero(GridLayout):
    def __init__(self, **kwargs):
        super(IngresarNumero, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Ingrese el número binario', size_hint=(0.2, 0.1), pos=(0, 0)))
        self.numeroInput = TextInput(multiline=False, size_hint=(2, 0.1), pos=(0, 10))
        self.add_widget(self.numeroInput)
        self.ingresar = Button(text="Analizar")
        self.ingresar.bind(on_press=self.press)
        self.add_widget(self.ingresar)

        x = 0
        y = 0
        plt.step(x, y)
        self.plot = FigureCanvasKivyAgg(plt.gcf())
        self.add_widget(self.plot)
    def press(self, instance):
        plt.clf()
        self.remove_widget(self.plot)
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        y = self.numeroInput.text
        y = [int(x) for x in y]
        plt.step(x, y)
        plt.xticks(x)
        plt.yticks([0, 1])
        self.plot = FigureCanvasKivyAgg(plt.gcf())
        self.add_widget(self.plot)

class GraphApp(App):
    def build(self):
        return IngresarNumero()


if __name__ == '__main__':
    GraphApp().run()


