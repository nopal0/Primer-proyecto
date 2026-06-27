def DiccionarioUsuario():
    UsDiccionario = {}
    with open ("datos/Usuarios.txt" , "r") as archivo:
        ArchivoLeido = archivo.read()
        ArchivoSeparadoPorLineas = ArchivoLeido.splitlines()
        for linea in ArchivoSeparadoPorLineas:
            dato = linea.split(":")
            UsuarioGuardado = dato[0]
            ContraseñaGuardada = dato [1]
            UsDiccionario[UsuarioGuardado] = ContraseñaGuardada
        return UsDiccionario
    
def DiccionarioDinero():
    DineroDiccionario = {}
    with open ("datos/Dinero.txt" , "r") as archivo:
        ArchivoLeido = archivo.read()
        ArchivoSeparadoPorLineas = ArchivoLeido.splitlines()
        for linea in ArchivoSeparadoPorLineas:
            dato = linea.split(":")
            UsuarioGuardado = dato[0]
            DineroGuardado = dato [1]
            DineroDiccionario[UsuarioGuardado] = DineroGuardado
        return DineroDiccionario