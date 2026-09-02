from pruebaj.DiccJson import leerDicc

def PedirU():
    u = input("Cual es tu usuario? ")
    return u

def validarU(u , DU):
    DU = leerDicc()
    
    if u in DU:
        return u
    else:
        return None

def PedirC():
    c = input("Cual es tu contraseña?")
    return c

def validarC(u , c , DU):
    if c == DU[u][c]:
        print("Incio de sesion correcto")
        return True
    else:
        print("No a sido posible iniciar sesion")
        False

def mainIN():
    DU = leerDicc()
    u = PedirU()
    u = validarU(u , DU)
    if u is not None:
        c = PedirC()
        validarC(u , c , DU)
        return True
    else:
        print("No ha sido posible iniciar sesion")
        return None

mainIN()