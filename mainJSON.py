from pruebaj.IN_JSON import mainIN
from pruebaj.Reg import mainRegistroJson
from funciones.validaciones import PedirNum
from funciones.dinero import mainDinero

def main():
    o = PedirNum("[1]Iniciar sesion [2Registro]")
    if o == 1:
        mainIN()
        mainDinero()
        
    elif o == 2:
        
        mainRegistroJson()
        mainDinero()
        
    else:
        print("")
        
main()