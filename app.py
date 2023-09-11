from data.data import *
from BD.baseDatos import *
from sklearn.linear_model import LinearRegression
from grafica.grafica import *
import pandas as pd

#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = base_teorico()

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos()
data_deformacion_2 = pd.DataFrame(data_list)
data_deformacion_2_fit = data_deformacion_2
X = data_deformacion_2_fit['Esfuerzo[kN]'].values.reshape(-1, 1)
y = data_deformacion_2_fit['Deformacion_2'].values.reshape(-1, 1)
x_lim = data_deformacion_2['Esfuerzo[kN]'].iloc[-1]
y_lim = data_deformacion_2['Deformacion_2'].iloc[-1]
model = LinearRegression()
model.fit(X, y)
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1)
print('la predicción a 1000 kN es de: ', prediction ,'mm')


dataRealEsfuerzo = data_deformacion_2['Esfuerzo[kN]']
dataRealDeformacion = data_deformacion_2['Deformacion[mm]']

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model)