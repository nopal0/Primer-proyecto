from pruebaj.IN_JSON import mainIN
from pruebaj.Reg import mainRegistroJson
from funciones.validaciones import PedirNum

def main():
    o = PedirNum("[1]Iniciar sesion" "[2Registro]")
    if o == 1:
        mainIN()
    elif o == 2:
        mainRegistroJson()
    else:
        print("")
        
main()