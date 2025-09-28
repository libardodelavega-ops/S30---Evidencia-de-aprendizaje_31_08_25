import pandas as pd
import kagglehub
import os
import zipfile
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter
# tkinter._test()
import numpy as np
class ejercicios:
    def __init__(self):
        datos = [(i, None) for i in range(1, 13)] 
        self.df= pd.DataFrame(data=datos,columns=["#ejercicio", "valor"])
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_Actividad_3 = "{}/Actividad_03/Salida_Archivos_Act_03".format(self.ruta_raiz)


    def ejercicio1(self):

        # Crea un DataFrame frutas
        fruta = pd.DataFrame({
            "Granadilla": [20],
            "Tomates": [50]})
        ruta_ej1 = os.path.join(self.ruta_Actividad_3, "Ejercicio_1.csv")
        fruta.to_csv(ruta_ej1, index=False)
        self.df.loc[0, "valor"] = ruta_ej1
        print(fruta)
        print("********************************************************************")

    def ejercicio2(self):
        # Crea un DataFrame ventas_frutas que coincida con el diagrama:
        ventas_frutas = pd.DataFrame(
    {"Granadilla": [20, 49], "Tomates": [50, 100]},
    index=["ventas 2021", "ventas 2022"])
        ruta_ej2 = os.path.join(self.ruta_Actividad_3, "Ejercicio_2.csv")
        ventas_frutas.to_csv(ruta_ej2, index=True)
        self.df.loc[1, "valor"] = ruta_ej2
        print(ventas_frutas)
        print("********************************************************************")

    def ejercicio3(self):
        #Crea una variable utensilios con una Serie que tenga el siguiente aspecto:
        utensilios = pd.Series(["Cuchara 3 unidades", 
                        "Tenedor 2 unidades", 
                        "Cuchillo 4 unidades", 
                        "Plato 5 unidades"], 
                        name="Cocina")
        ruta_ej3 = os.path.join(self.ruta_Actividad_3, "Ejercicio_3.csv")
        utensilios.to_csv(ruta_ej3, index=False)
        self.df.loc[2, "valor"] = ruta_ej3
        print(utensilios)
        print("********************************************************************")
