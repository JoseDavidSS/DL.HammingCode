from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from HammingLogic import HammingLogic


class tablesGrid(GridLayout):
    def __init__(self, **kwargs):
        super(tablesGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Ingrese el número binario', size_hint=(0.2, 0.1), pos=(0, 0)))
        self.numeroInput = TextInput(multiline=False, size_hint=(2, 0.1), pos=(0, 10))
        self.add_widget(self.numeroInput)
        self.ingresar = Button(text="Analizar")
        self.ingresar.bind(on_press=self.press)
        self.add_widget(self.ingresar)
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                      size_hint=(1, 1),
                                      rows_num=7,
                                      column_data=[
                                      ],
                                      row_data=[]
                                      )


    def press(self, instance):
        mat = HammingLogic.hamming(self.numeroInput.text)
        ind = ["Original", "p1", "p2", "p3", "p4", "p5", "Final"]
        for idx, x in enumerate(mat):
            x.insert(0, ind[idx])
        for x in mat:
            print(x)
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(1, 1),
                                 rows_num=7,
                                 column_data=[
                                     ("  ", dp(18)),
                                     ("P1", dp(18)),
                                     ("P2", dp(18)),
                                     ("d1", dp(18)),
                                     ("P3", dp(18)),
                                     ("d2", dp(18)),
                                     ("d3", dp(18)),
                                     ("d4", dp(18)),
                                     ("P4", dp(18)),
                                     ("d5", dp(18)),
                                     ("d6", dp(18)),
                                     ("d7", dp(18)),
                                     ("d8", dp(18)),
                                     ("d9", dp(18)),
                                     ("d10", dp(18)),
                                     ("d11", dp(18)),
                                     ("P5", dp(18)),
                                     ("d12", dp(18))
                                 ],
                                 row_data=mat
                                 )
        self.add_widget(self.data_table)


class MyApp(MDApp):
    def build(self):
        return tablesGrid()