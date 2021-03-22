from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from HammingLogic import HammingLogic


class tablesGrid(GridLayout):
    def __init__(self, **kwargs):
        super(tablesGrid, self).__init__(**kwargs)
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 30

        # tablesBodyGrid
        self.tablesBody = GridLayout(
            row_force_default = True,
            row_default_height = 30,
            col_force_default = True,
            col_default_width = 300)
        self.tablesBody.cols = 3

        self.tablesBody.add_widget(Label(text='Ingrese el número binario', size_hint=(0.2, 0.1), pos=(0, 0)))
        self.numeroInput = TextInput(multiline=False, size_hint=(2, 0.1), pos=(0, 10))
        self.tablesBody.add_widget(self.numeroInput)
        self.ingresar = Button(text="Analizar")
        self.ingresar.bind(on_press=self.press)
        self.tablesBody.add_widget(self.ingresar)

        self.add_widget(self.tablesBody)

        # tablesBody2Grid
        self.tablesBody2 = GridLayout(
            row_force_default = True,
            row_default_height = 30,
            col_force_default = True,
            col_default_width = 300)
        self.tablesBody2.cols = 2

        self.tablesBody2.add_widget(Label(text='Paridad par ?:', size_hint=(0.2, 0.1), pos=(0, 0)))
        self.parityCheckBox = CheckBox()
        self.tablesBody2.add_widget(self.parityCheckBox)

        self.tablesBody2.add_widget(Label(text='Ingrese la posción del bit a cambiar:', size_hint=(0.2, 0.1), pos=(0, 0)))
        self.posBit = TextInput(multiline=False, size_hint=(2, 0.1), pos=(0, 10))
        self.tablesBody2.add_widget(self.posBit)

        self.add_widget(self.tablesBody2)

        #Create first table grid
        self.firstTableGrid = GridLayout(
            row_force_default = True,
            row_default_height = 300,
            col_force_default = True,
            col_default_width = 900)
        self.firstTableGrid.cols = 1

        #Create second table grid
        self.secondTableGrid = GridLayout(
            row_force_default = True,
            row_default_height = 300,
            col_force_default = True,
            col_default_width = 900)
        self.secondTableGrid.cols = 1

        #Add table grids
        self.add_widget(self.firstTableGrid)
        self.add_widget(self.secondTableGrid)

        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                      size_hint=(0.5, 0.5),
                                      rows_num=7,
                                      column_data=[
                                      ],
                                      row_data=[]
                                      )

        self.data_table2 = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                      size_hint=(0.5, 0.5),
                                      rows_num=7,
                                      column_data=[
                                      ],
                                      row_data=[]
                                      )

    def press(self, instance):
        Window.size = (900, 700)
        HammingLogic.paridad = self.parityCheckBox.active



        val = self.numeroInput.text

        for i in val:
            if int(i) == 0 or int(i)==1:
                pass
            else:
                print("Numero no binario")
                return None

        if (len(val) != 12):
            print("El número no es de 12 bits")
            return None

        mat = HammingLogic.hamming(val)

        posError = int(self.posBit.text) - 1

        hammingFinal = mat[6][:]


        if hammingFinal[posError] == "1":
            hammingFinal[posError] = "0"
        elif hammingFinal[posError] == "0":
            hammingFinal[posError] = "1"

        listError = HammingLogic.calcularBitErroneo([int(i) for i in hammingFinal])
        ind = ["Original", "p1", "p2", "p3", "p4", "p5", "Final"]
        for idx, x in enumerate(mat):
            x.insert(0, ind[idx])
        for x in mat:
            print(x)

        matError = mat[:]

        # Cambiar la tabla con el error
        conError = 0

        ancho = 8
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(0.9, 0.6),
                                 rows_num=7,
                                 column_data=[
                                     ("  ", dp(14)),
                                     ("P1", dp(ancho)),
                                     ("P2", dp(ancho)),
                                     ("d1", dp(ancho)),
                                     ("P3", dp(ancho)),
                                     ("d2", dp(ancho)),
                                     ("d3", dp(ancho)),
                                     ("d4", dp(ancho)),
                                     ("P4", dp(ancho)),
                                     ("d5", dp(ancho)),
                                     ("d6", dp(ancho)),
                                     ("d7", dp(ancho)),
                                     ("d8", dp(ancho)),
                                     ("d9", dp(ancho)),
                                     ("d10", dp(ancho)),
                                     ("d11", dp(ancho)),
                                     ("P5", dp(ancho)),
                                     ("d12", dp(ancho))
                                 ],
                                 row_data=mat
                                 )
        self.firstTableGrid.add_widget(self.data_table)

        for cont, x in enumerate(matError):
            if cont == 0 or cont == 6:
                x.append("")
            else:
                x.append(listError[conError])
                conError += 1
            for idx, y in enumerate(x):
                if idx == posError+1:
                    if y == "1":
                        x[idx] = "0"
                    elif y == "0":
                        x[idx] = "1"

        self.data_table2 = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                      size_hint=(0.5, 0.5),
                                      rows_num=7,
                                      column_data=[
                                          ("  ", dp(14)),
                                          ("P1", dp(ancho)),
                                          ("P2", dp(ancho)),
                                          ("d1", dp(ancho)),
                                          ("P3", dp(ancho)),
                                          ("d2", dp(ancho)),
                                          ("d3", dp(ancho)),
                                          ("d4", dp(ancho)),
                                          ("P4", dp(ancho)),
                                          ("d5", dp(ancho)),
                                          ("d6", dp(ancho)),
                                          ("d7", dp(ancho)),
                                          ("d8", dp(ancho)),
                                          ("d9", dp(ancho)),
                                          ("d10", dp(ancho)),
                                          ("d11", dp(ancho)),
                                          ("P5", dp(ancho)),
                                          ("d12", dp(ancho)),
                                          ("Error", dp(9))
                                      ],
                                      row_data=matError
                                      )
        self.firstTableGrid.add_widget(self.data_table2)


class MyApp(MDApp):
    def build(self):
        return tablesGrid()