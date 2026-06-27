

def OpcionesPrincipalesDinero():
    Opcion1 = ["Retirar dinero[1]: " , "Depositar dinero[2]: " , "Salir[3]: "]
    
    for linea in Opcion1:
        print(linea)

def MostrarOpciones():
    OpcionesRegistro = ["[1]Iniciar sesion: ","[2]1Salir de la aplicacion: "]
    
    for linea in OpcionesRegistro:
        print(linea)
        
def Desicion1():
        Decision = input("Registro exitoso que quieres hacer ahora?")
        if Decision == "1":
            return 1
        elif Decision == "2":
            print('Saliendo del sistema...')
        else:
            print("Valor incorrecto intete mas tarde")
