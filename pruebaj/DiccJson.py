import json

def leerDicc():
    with open ("mi_base_datos.json", "r") as archivo:
        DU = json.load(archivo) 
        return DU

def cambiarDinero(u , d ):
    with open ("mi_base_datos.json", "r") as archivo:
        DU = json.load(archivo)
        
        DU[u] = d
        
    with open ("mi_base_datos.json", "w") as archivo:
        json.dump(DU , archivo)