def ValidarQueSeaNum():
    try:
        cantidad = int(input("De que monto sera el movimiento a realizar?: "))
        return cantidad
    except ValueError:
        print("Error: Se debe de ingresar un numero")
        return None
    
def ValidarNumPositivo(cantidad):
    if cantidad > 0:
        return True
    else:
        print("Ingrese un numero positivo")
        return False
    
def PedirNum(pregunta):
    
    o = 4
    
    while o > 0:
        try:
            ca = int(input(pregunta))
            return ca
        except ValueError:
            o -= 1
            print("Error: Se debe de ingresar un numero")
            if o == 0:
                print("Sin intentos posibles intentelo mas tarde")
                return None
    