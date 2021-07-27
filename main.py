import copy

import codecs
import shutil
from pathlib import Path
import os
from xml.dom import minidom
from Funciones.crear_carpetas import crear_carpeta
from Funciones.modifica_svg import prepara_carton_svg, svgtopng, prepara_carton_svg2, prepara_hoja_carton
from Funciones.numerador import generar_carton, generar_plancha, generar_hoja_carton
from Funciones.varios import saca_x

salida = "output"
svg_base = "Carton_base.svg"
hoja_carton_base = "Hoja_carton_base.svg"
png_vacio = "vacio.png"
base_dir = Path(__file__).resolve().parent
salida_dir = crear_carpeta(salida, base_dir)
bases = os.path.join(base_dir, "svgs")
carton_svg = os.path.join(bases, svg_base)
vaciopng_path = os.path.join(bases, png_vacio)

temp = crear_carpeta("temp", salida_dir)
rec_vacio = os.path.join(bases, "rect_vacio.svg")
png = svgtopng(rec_vacio, temp, "vacio.png")
# shutil.copy(vaciopng_path, temp)

hoja_base_svg = os.path.join(bases, hoja_carton_base)
copia_hoja = os.path.join(bases, "copia.svg")
copia_base = shutil.copy(hoja_base_svg, copia_hoja)
lista_cartones1 = generar_hoja_carton()
lista_cartones2 = generar_hoja_carton()
lista_cartones = lista_cartones1 + lista_cartones2
prepara_hoja_carton(hoja_base_svg, temp, "%c", "%", "prueba1.svg", vaciopng_path, lista_cartones)

lista_hojas = []
for x in range(10):
    lista_hojas.append(generar_hoja_carton())

print(len(generar_hoja_carton()))
print(len(lista_hojas))
# svg = prepara_carton_svg(carton_svg, temp, "%b", "%", "name_svg.svg", vaciopng_path)
# svgtopng(svg, salida_dir, "name_png")
# for x in range(10):
#     name_svg = "carton" + str(x) + ".svg"
#     name_png = "carton" + str(x) + ".png"
#     svg = prepara_carton_svg(carton_svg, temp, "%b", "%", name_svg, vaciopng_path)
#     svgtopng(svg, salida_dir, name_png)
#
# shutil.rmtree(temp)

lista_carton = []
# for x in range(6):
#     carton = generar_carton()
#     print(carton)
#     c2 = carton
#     # c2 = saca_x(c2)
#     rep = 0
#     if carton not in lista_carton:
#         # for lcarton in lista_carton:
#         #     l_carton = lista_carton
#         #     l_carton = saca_x(l_carton)
#         #     for num_c in c2:
#         #         if num_c in l_carton:
#         #             rep = 1
#         if rep == 0:
#             print(carton)
#             lista_carton.append(carton)
# print(lista_carton)
# x = 1
# for cart in lista_carton:
#     # print(cart)
#     name_svg = "carton" + str(x) + ".svg"
#     name_png = "carton" + str(x) + ".png"
#     svg = prepara_carton_svg2(carton_svg, temp, "%b", "%", name_svg, vaciopng_path, cart)
#     svgtopng(svg, salida_dir, name_png)
#     x = x + 1
#
# shutil.rmtree(temp)

#
# print("'''''''''''''''")
# print(lista_carton)
# print(len(lista_carton))

# svgtopng(svg, salida_dir, "name_png")
# print(carton)
# pos = 0
# for digit in carton:
#     if digit == 'X':
#         del carton[pos]
#     pos = pos + 1
# pos = 0
# for digit in carton:
#     if digit == 'X':
#         del carton[pos]
#     pos = pos + 1
# for digit in carton:
#     if digit == 'X':
#         del carton[pos]
#     pos = pos + 1
#
# print(carton)



# carton = generar_carton()
# print(carton)
# c2 = saca_x(carton)
list1 = generar_plancha(5)
# print(len(list1))
# if carton in list1:
#     print("ok")
# else:
#     print("no ok")