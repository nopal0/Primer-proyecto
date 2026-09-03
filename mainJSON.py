from pruebaj.IN_JSON import mainIN
from pruebaj.Reg import mainRegistroJson
from funciones.validaciones import PedirNum
from funciones.dinero import mainDinero

def main():
    o = PedirNum("[1]Iniciar sesion [2Registro]")
    if o == 1:
        u = mainIN()
        mainDinero(u)
        
    elif o == 2:
        
        u = mainRegistroJson()
        mainDinero(u)
        
    else:
        print("")
        
main()