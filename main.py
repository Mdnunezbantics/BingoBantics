import copy

import codecs
import shutil
from pathlib import Path
import os
from xml.dom import minidom

import cairosvg
from merge_pdf import merge

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

temp_svg = crear_carpeta("temp_svg", salida_dir)
rec_vacio = os.path.join(bases, "rect_vacio.svg")
png = svgtopng(rec_vacio, temp_svg, "vacio.png")
# shutil.copy(vaciopng_path, temp)

hoja_base_svg = os.path.join(bases, hoja_carton_base)
copia_hoja = os.path.join(bases, "copia.svg")
copia_base = shutil.copy(hoja_base_svg, copia_hoja)
# lista_cartones1 = generar_hoja_carton()
# lista_cartones2 = generar_hoja_carton()
# lista_cartones = lista_cartones1 + lista_cartones2
# prepara_hoja_carton(hoja_base_svg, temp, "%c", "%", "pruebaxxxxx.svg", vaciopng_path, lista_cartones)

lista_hojas = []
cantidad_hojas = 10
item = []
lista_cartones = []
# un minuto en hacer la lista sin svg
for page in range(cantidad_hojas):
    cartones_para_hoja = []
    # print(page)
    for x in range(2):
        item = generar_hoja_carton()
        while item in lista_hojas:
            item = generar_hoja_carton()
        cartones_para_hoja = cartones_para_hoja + item
        lista_hojas.append(item)
        # cartones_para_hoja.append(item)
    # print(item)
    lista_cartones.append(cartones_para_hoja)

page = 0
for hojita in lista_cartones:
    page = page + 1
    prepara_hoja_carton(hoja_base_svg, temp_svg, "%c", "%", str(page) + "prueba" + ".svg", vaciopng_path, hojita)


# print("--------------")
# print(len(lista_hojas))
# print("--------------")
temp_pdf = crear_carpeta("temp_pdf", salida_dir)
list_svg_dir = os.listdir(temp_svg)
file_list = []
list_svg_dir.sort()
for file in list_svg_dir:
    if ".svg" in file:
        file_svg = os.path.join(temp_svg, file)
        file_pdf = os.path.join(temp_pdf, file[:-4] + ".pdf")
        cairosvg.svg2pdf(file_obj=open(file_svg, "rb"), write_to=file_pdf)
        # print(file)


pdf_file_name = "bingo.pdf"
pdf_output = os.path.join(salida_dir, pdf_file_name)

merge.Merge(pdf_output).merge_folder(temp_pdf)

print("fusionado")



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