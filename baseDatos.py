from pymongo.mongo_client import MongoClient

#CONEXIÓN
def conexion():
    uri = "mongodb+srv://davidmateo0509:1234@cluster0.afpjypb.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    return MongoClient(uri)

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos():
    client = conexion()
    data_base= client.actividad4.data_deformacion_2
    data_list = []
    for data_deformacion_2_data_base in data_base.find():
        data_list.append(data_deformacion_2_data_base)    
    return data_list

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""