import copy
import random
import numpy as np
from numpy.random import choice


## Meto la matriz, tengo que quitarle 12 aleatoriamente de los 27 totales para que se queden en 15
from Funciones.varios import saca_x


def generar_carton():
    lst1 = sorted(random.sample(range(1, 9), 3))
    lst2 = sorted(random.sample(range(10, 19), 3))
    lst3 = sorted(random.sample(range(20, 29), 3))
    lst4 = sorted(random.sample(range(30, 39), 3))
    lst5 = sorted(random.sample(range(40, 49), 3))
    lst6 = sorted(random.sample(range(50, 59), 3))
    lst7 = sorted(random.sample(range(60, 69), 3))
    lst8 = sorted(random.sample(range(70, 79), 3))
    lst9 = sorted(random.sample(range(80, 90), 3))

    ## metemos en todas t_list_1 menos en 1,3,6 (así es como aparece en los cartones)
    t_list = ['X']
    t_list_2 = ['X', 'X']

    def swap_elements_1(x, t):
        new_x = x
        for idx, value in zip(choice(range(len(x)), size=len(t), replace=False), t_list):
            new_x[idx] = value
        return new_x

    def swap_elements_2(x, t):
        new_x = x
        for idx, value in zip(choice(range(len(x)), size=len(t), replace=False), t_list_2):
            new_x[idx] = value
        return new_x

    uno = swap_elements_2(lst1, t_list_2)
    dos = swap_elements_1(lst2, t_list)
    tres = swap_elements_2(lst3, t_list_2)
    cuatro = swap_elements_1(lst4, t_list)
    cinco = swap_elements_1(lst5, t_list)
    seis = swap_elements_2(lst6, t_list_2)
    siete = swap_elements_1(lst7, t_list)
    ocho = swap_elements_1(lst8, t_list)
    nueve = swap_elements_1(lst9, t_list)
    numeracion = [uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve]
    # matriz = np.array([uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve])
    # matriz_transpuesta = matriz.transpose()
    #
    # for elementos in matriz_transpuesta:
    #     print(elementos)
    carton = []
    for fila in numeracion:
        for digito in fila:
            carton.append(str(digito))
    return carton


def generar_hoja_carton():
    forma_col_1 = ["X"]
    forma_col_2 = ["X", "X"]

    nums1 = ["1",   "2",  "3",  "4",  "5",  "6",  "7",  "8",  "9"]
    nums2 = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]
    nums3 = ["20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]
    nums4 = ["30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]
    nums5 = ["40", "41", "42", "43", "44", "45", "46", "47", "48", "49"]
    nums6 = ["50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]
    nums7 = ["60", "61", "62", "63", "64", "65", "66", "67", "68", "69"]
    nums8 = ["70", "71", "72", "73", "74", "75", "76", "77", "78", "79"]
    nums9 = ["80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90"]
    numeros = [nums1, nums2, nums3, nums4, nums5, nums6, nums7, nums8, nums9]

    cols1 = ["2", "1", "2", "1", "2", "1"]
    cols2 = ["1", "2", "1", "1", "1", "2"]
    cols3 = ["2", "1", "1", "2", "1", "1"]
    cols4 = ["1", "2", "2", "1", "1", "1"]
    cols5 = ["1", "1", "1", "1", "2", "2"]
    cols6 = ["1", "1", "2", "2", "1", "1"]
    cols7 = ["1", "2", "1", "1", "2", "1"]
    cols8 = ["1", "1", "1", "2", "1", "2"]
    cols9 = ["2", "1", "1", "1", "1", "1"]
    cols = [cols1, cols2, cols3, cols4, cols5, cols6, cols7, cols8, cols9]

    carton1 = []
    carton2 = []
    carton3 = []
    carton4 = []
    carton5 = []
    carton6 = []
    hoja = [carton1, carton2, carton3, carton4, carton5, carton6]

    columna_1 = []
    columna_2 = []
    columna_3 = []
    columna_4 = []
    columna_5 = []
    columna_6 = []
    columna_7 = []
    columna_8 = []
    columna_9 = []
    columnas = [columna_1, columna_2, columna_3, columna_4, columna_5, columna_6, columna_7, columna_8, columna_9]

    for indi in range(9):
        colum = cols[indi]
        num = numeros[indi]
        for x in range(6):
            columna = []
            col = choice(colum)
            colum.remove(col)
            if col == "2":
                columna = copy.copy(forma_col_2)
                f1 = choice(num)
                num.remove(f1)
                columna.append(f1)
            if col == "1":
                columna = copy.copy(forma_col_1)
                f1 = choice(num)
                num.remove(f1)
                f2 = choice(num)
                num.remove(f2)
                columna.append(f1)
                columna.append(f2)
            random.shuffle(columna)
            columnas[indi].append(columna)

    for num in range(6):
        for col in columnas:
            # print(col[num])
            hoja[num].append(col[num])
    cartones = []
    for num in range(6):
        cart = []
        carton = copy.copy(hoja[num])
        hoja[num] = []
        for fila in carton:
            for digito in fila:
                cart.append(str(digito))
        cartones.append(cart)
        hoja[num] = cart
    return cartones


list_carton_general = []


def generar_plancha(cantidad):
    list_carton_hoja = []
    rep = 0
    # for x in range(cantidad):
    #     carton = generar_carton()
    #     while carton in list_carton_general:
    #         carton = generar_carton()
    #     while len(list_carton_hoja) < cantidad:
    #         rep = 0
    #         cart_1 = saca_x(carton)
    #         for cart_list in list_carton_hoja:
    #             cart_2 = saca_x(cart_list)
    #             for digit_clist in cart_2:
    #                 for digit_c in cart_1:
    #                     # print(digit_c, digit_clist)
    #                     if str(digit_c) == str(digit_clist):
    #                         rep = 1
    #         if rep == 1:
    #             carton = generar_carton()
    #             while carton in list_carton_general:
    #                 carton = generar_carton()
    #         else:
    #             list_carton_hoja.append(carton)
    #             list_carton_general.append(carton)
    #             print(carton)


        # else:
            # c = saca_x(carton)
            # b = 0
            # for a in c:
            #     b = int(a) + b
            # print(b)
            # rep = "ok"


    # print(list_carton_hoja)
    # print(len(list_carton_hoja))
    return list_carton_general
