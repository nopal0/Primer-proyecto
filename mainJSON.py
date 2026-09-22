from funciones.IN_JSON import mainIN
from funciones.Reg import mainRegistroJson
from funciones.validaciones import PedirNum
from funciones.dinero import mainDinero

def main():

    op = 5

    while op > 0:

        print("Bienvenido a mcbank")
        o = PedirNum("[1]Iniciar sesion [2Registro]")
        
        if o == 1:

            u = mainIN()

            if u is not None:

                mainDinero(u)

            else:
                print("No se a podido iniciar sesion vuelva mas tarde")
                    
        elif o == 2:
            
            u = mainRegistroJson()
            if u is not None:

                mainDinero(u)
            
        else:

            op -= 1
            print("Esa opcion no es valida, intente de nuevo")

            if op == 0:
                print("Demasiados intentos, vuelva mas tarde")
       
main()