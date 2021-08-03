import copy
from numpy.random import choice
from random import shuffle
from Funciones.varios import saca_x

list_carton_general = []


def generar_hoja_carton():
    patron1 = ["2", "4", "6", "8", "11", "12", "13", "15", "16", "17", "20", "21", "22", "24", "25"]
    patron2 = ["2", "3", "5", "7", "9", "10", "14", "15", "16", "18", "19", "22", "23", "26", "27"]
    patron3 = ["2", "4", "6", "7", "8", "12", "13", "15", "17", "20", "21", "22", "24", "25", "26"]
    patron4 = ["2", "3", "4", "5", "9", "10", "11", "14", "15", "16", "19", "21", "22", "26", "27"]
    patron5 = ["3", "4", "6", "7", "8", "11", "12", "15", "16", "17", "20", "22", "24", "25", "26"]
    patron6 = ["2", "3", "4", "7", "9", "10", "11", "14", "16", "18", "19", "21", "23", "26", "27"]
    patrones = [patron1, patron2, patron3, patron4, patron5, patron6]

    nums1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    nums2 = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]
    nums3 = ["20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]
    nums4 = ["30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]
    nums5 = ["40", "41", "42", "43", "44", "45", "46", "47", "48", "49"]
    nums6 = ["50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]
    nums7 = ["60", "61", "62", "63", "64", "65", "66", "67", "68", "69"]
    nums8 = ["70", "71", "72", "73", "74", "75", "76", "77", "78", "79"]
    nums9 = ["80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90"]
    cartones = []
    shuffle(patrones)
    check_cartones = False
    finalizar = False
    while not finalizar:
        check_cartones = False
        for patron in patrones:
            casilla = 1
            casillax = 1
            carton = []
            while casilla <= 27:
                if str(casilla) in patron:
                    if casilla == 1 or casilla == 2 or casilla == 3:
                        num = choice(nums1)
                        nums1.remove(num)
                        carton.append(int(num))
                    if casilla == 4 or casilla == 5 or casilla == 6:
                        num = choice(nums2)
                        nums2.remove(num)
                        carton.append(int(num))
                    if casilla == 7 or casilla == 8 or casilla == 9:
                        num = choice(nums3)
                        nums3.remove(num)
                        carton.append(int(num))
                    if casilla == 10 or casilla == 11 or casilla == 12:
                        num = choice(nums4)
                        nums4.remove(num)
                        carton.append(int(num))
                    if casilla == 13 or casilla == 14 or casilla == 15:
                        num = choice(nums5)
                        nums5.remove(num)
                        carton.append(int(num))
                    if casilla == 16 or casilla == 17 or casilla == 18:
                        num = choice(nums6)
                        nums6.remove(num)
                        carton.append(int(num))
                    if casilla == 19 or casilla == 20 or casilla == 21:
                        num = choice(nums7)
                        nums7.remove(num)
                        carton.append(int(num))
                    if casilla == 22 or casilla == 23 or casilla == 24:
                        num = choice(nums8)
                        nums8.remove(num)
                        carton.append(int(num))
                    if casilla == 25 or casilla == 26 or casilla == 27:
                        num = choice(nums9)
                        nums9.remove(num)
                        carton.append(int(num))

                casilla = casilla + 1
            carton.sort()
            while casillax <= 27:
                if str(casillax) not in patron:
                    carton.insert(casillax - 1, "X")
                casillax = casillax + 1

            cartones.append(carton)
        for c1 in cartones:
            check = saca_x(copy.copy(c1))
            check.sort()

            if check not in list_carton_general:
                print(check)
                list_carton_general.append(check)
            else:
                print("repe")
                check_cartones = True
        if not check_cartones:
            finalizar = True

    return cartones
