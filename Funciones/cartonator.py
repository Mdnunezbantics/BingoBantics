import random
import numpy as np
from numpy.random import choice

## Meto la matriz, tengo que quitarle 12 aleatoriamente de los 27 totales para que se queden en 15
def generar_carton():
    lst1 = sorted(random.sample(range(9), 3))
    lst2 = sorted(random.sample(range(10, 19), 3))
    lst3 = sorted(random.sample(range(20, 29), 3))
    lst4 = sorted(random.sample(range(30, 39), 3))
    lst5 = sorted(random.sample(range(40, 49), 3))
    lst6 = sorted(random.sample(range(50, 59), 3))
    lst7 = sorted(random.sample(range(60, 69), 3))
    lst8 = sorted(random.sample(range(70, 79), 3))
    lst9 = sorted(random.sample(range(80, 89), 3))

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

    uno = swap_elements_2(lst1 , t_list_2)
    dos = swap_elements_1(lst2 , t_list)
    tres = swap_elements_2(lst3 , t_list_2)
    cuatro = swap_elements_1(lst4 , t_list)
    cinco = swap_elements_1(lst5 , t_list)
    seis = swap_elements_2(lst6 , t_list_2)
    siete = swap_elements_1(lst7 , t_list)
    ocho = swap_elements_1(lst8 , t_list)
    nueve = swap_elements_1(lst9 , t_list)
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