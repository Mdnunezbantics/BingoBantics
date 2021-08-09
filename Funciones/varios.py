import copy


def saca_x(dato):
    carton2 = copy.copy(dato)
    pos = 0
    for digit in carton2:
        if digit == "X":
            del dato[pos]
        else:
            pos = pos + 1
    return dato


def completa_numero(catidad_digitos, dato):
    if catidad_digitos != 1:
        while len(str(dato)) != catidad_digitos:
            dato = str(0) + str(dato)
    else:
        dato = dato
    return dato
