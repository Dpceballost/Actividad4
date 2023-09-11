import pandas as pd

# Importar datos del csv
base_teorico = pd.read_csv(r"C:\Daniela\10 semestre\Programación II\Mongo\Data ingeniero_proyecto.csv")

#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def base_teorico():
    dataTeoricoEsfuerzo = base_teorico['Esfuerzo[kN]']
    dataTeoricoDeformacion = base_teorico['Deformacion_2']
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion