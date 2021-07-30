import datos_variables
from Funciones.numerador import generar_hoja_carton

def crear_lista_cartones(cantidad_hojas,):

    lista_cartones = []
    lista_hojas = []
    a = 0
    item = []
    for page in range(cantidad_hojas):
        cartones_para_hoja = []
        for x in range(2):
            item = generar_hoja_carton()
            while item in lista_hojas:
                item = generar_hoja_carton()
            cartones_para_hoja = cartones_para_hoja + item
            lista_hojas.append(item)
        if a == 500:
            a = 1
        else:
            a = a + 1
        lista_cartones.append(cartones_para_hoja)
    return lista_cartones, lista_hojas