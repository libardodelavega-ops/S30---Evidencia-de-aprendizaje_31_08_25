# entregable_dos.py
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import os

class Entregable_dos():

    def obtener_datos_kaggle(self, dataset_name="zadafiyabhrami/global-crocodile-species-dataset"):
        """
        Descarga el dataset con kagglehub y lo carga en un DataFrame.
        """
        path = kagglehub.dataset_download(dataset_name)
        print("✅ Path del dataset:", path)

        # Busca el primer archivo CSV dentro de la carpeta descargada
        csv_file = None
        for file in os.listdir(path):
            if file.endswith(".csv"):
                csv_file = os.path.join(path, file)
                break

        if not csv_file:
            print("❌ No se encontró archivo CSV en el dataset.")
            return pd.DataFrame()

        df = pd.read_csv(csv_file)
        return df
    
    def enriquecer_df(self, df=pd.DataFrame()):
        """
        Agrega columnas adicionales al dataset de cocodrilos.
        """
        if df.empty:
            print("❌ DataFrame vacío.")
            return df
        
        # Ejemplo: clasificar por tamaño si existe la columna "Length_m" o similar
        if "Length_m" in df.columns:
            def size_category(length):
                if length < 2:
                    return "Pequeño"
                elif length < 4:
                    return "Mediano"
                else:
                    return "Grande"
            df["Size_Category"] = df["Length_m"].apply(size_category)

        return df
    
    def generar_imagenes(self, df=pd.DataFrame()):
        """
        Genera gráficos básicos con datos del dataset de cocodrilos.
        """
        if df.empty:
            print("❌ DataFrame vacío. No se pueden generar gráficos.")
            return
        print("✅ Generando gráficos...")

        fig, axes = plt.subplots(1, 3, figsize=(18, 5))

        # Gráfico 1: Conteo por especie
        if "Species" in df.columns:
            df["Species"].value_counts().plot(kind="bar", ax=axes[0], title="Distribución de Especies", color="green")
        else:
            axes[0].text(0.5, 0.5, 'Columna Species faltante', ha='center')

        # Gráfico 2: Histograma de longitudes
        if "Length_m" in df.columns:
            df["Length_m"].plot(kind="hist", bins=10, ax=axes[1], title="Histograma de Longitudes", color="blue", edgecolor="black")
        else:
            axes[1].text(0.5, 0.5, 'Columna Length_m faltante', ha='center')

        # Gráfico 3: Conteo por país (si existe)
        if "Country" in df.columns:
            df["Country"].value_counts().head(10).plot(kind="bar", ax=axes[2], title="Top 10 Países con Cocodrilos", color="orange")
        else:
            axes[2].text(0.5, 0.5, 'Columna Country faltante', ha='center')

        plt.tight_layout()
        plt.savefig("entregable2_crocodiles.jpg")
        print("✅ Gráfico guardado como 'entregable2_crocodiles.jpg'")    


# ------------------- EJECUCIÓN -------------------

entdos = Entregable_dos()
df = entdos.obtener_datos_kaggle("zadafiyabhrami/global-crocodile-species-dataset")
print(df.head(2))
print("*****************************************************************************************************************************")

df = entdos.enriquecer_df(df)
print(df.head(2))
print("*****************************************************************************************************************************")

df.to_csv("datos_cocodrilos.csv", index=False)
entdos.generar_imagenes(df)
