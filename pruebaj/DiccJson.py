import json

def leerDicc():
    with open ("mi_base_datos.json", "r") as archivo:
        DU = json.load(archivo) 
        return DU
