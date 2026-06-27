from funciones.diccionarios import DiccionarioUsuario
from funciones.login import mainInicioDeSesion
from funciones.dinero import mainDinero
from funciones.registro import mainRegistro

def main():
    Opciones = ["[1]Iniciar sesion: " , "[2]Registrarme: "]
    for linea in Opciones:
        print(linea)
    Decision = int(input("Que quieres hacer?"))
    if Decision == 1:
        DiccUsuario = DiccionarioUsuario()
        usuario = mainInicioDeSesion()
        if usuario in DiccUsuario:
            mainDinero(usuario)
        else:
            print("Usuario o contraseña incorrectos")
    elif Decision == 2:
        mainRegistro()
    else:
        print("Error intente mas tarde")
        
main()