import copy
import shutil
from pathlib import Path
import os

import crear_lista_cartones
import datos_variables
from Funciones.crear_carpetas import crear_carpeta
from Funciones.modifica_svg import svgtopng, prepara_hoja_carton, multi_svgs_a_1_pdf, prepara_svg_para_pdf2, unesvg_png
from Funciones.numerador import generar_hoja_carton
from Funciones.varios import completa_numero
from crear_pdf import hacer_pdfs
from crear_trabajo_completo import trabajo_completo

print("inicio")
# trabajo_completo()
print("fin")
print("inicio")
hacer_pdfs()
print("inicio")
# base_dir = Path(__file__).resolve().parent
#
# cantidad_hojas = datos_variables.cantidad_hojas
# hojas_por_pdf = datos_variables.hojas_por_pdf
# lista_hojas = crear_lista_cartones.lista_hojas
# lista_cartones = crear_lista_cartones.lista_cartones
# salida = datos_variables.salida
# svg_base = datos_variables.svg_base
# hoja_carton_base = datos_variables.hoja_carton_base
# hoja_datos_variables = datos_variables.hoja_datos_variables
# hoja_base_12_cartones = datos_variables.hoja_base_12_cartones
# png_vacio = datos_variables.png_vacio
#
# if salida in os.listdir(base_dir):
#     print("se encotro carpeta la eliminaremos")
#     shutil.rmtree(os.path.join(base_dir, salida))
# print("se crea carpeta output")
# salida_dir = crear_carpeta(salida, base_dir)
# bases = os.path.join(base_dir, "svgs")
# rec_vacio = os.path.join(bases, "rect_vacio.svg")
# hoja_base_svg = os.path.join(bases, hoja_carton_base)
# hoja_datos_variables_svg = os.path.join(bases, hoja_datos_variables)
# hoja_base_12_cartones_svg = os.path.join(bases, hoja_base_12_cartones)
#
#
# print("Generamos cartones")
#
# print("Cartones Listos")
# print("Preparamos PDFS")
# pdf = 1
# page = 0
# tira1 = 0
# tira2 = cantidad_hojas
# carton_id = 1
# carton_id2 = (cantidad_hojas * 6) + 1
# print("Se crea carpeta_svgs" + completa_numero(5, pdf))
# # temp_svg = crear_carpeta("carpeta_svgs" + completa_numero(5, pdf), salida_dir)
# temp_svg2 = crear_carpeta("carpeta_svgs2" + completa_numero(5, pdf), salida_dir)
# temp_final = crear_carpeta("carpeta_svgsfinal" + completa_numero(5, pdf), salida_dir)
# dir_pngs = crear_carpeta("carpeta_pngs" + completa_numero(5, pdf), salida_dir)
# png = svgtopng(rec_vacio, bases, png_vacio)
# print("Preparandos PDFS", " desde ", str(copy.copy(tira1)), " hasta ", str(copy.copy(tira1) + 100))
# for hoja_carton in lista_cartones:
#     print(page)
#     page = page + 1
#     hoja = completa_numero(5, page)
#     hoja_png_name = "png" + str(hoja) + ".png"
#     # prepara_hoja_carton(hoja_base_svg, temp_svg, "%c", "%", "svg" + str(hoja) + ".svg", png, hoja_carton, tira1,
#     #                     tira2, carton_id, carton_id2)
#     hoja_svg = prepara_hoja_carton(hoja_base_12_cartones_svg, temp_svg2, "%c", "%", "svg" + str(hoja) + ".svg", png, hoja_carton, tira1,
#                         tira2, carton_id, carton_id2)
#     hoja_png = svgtopng(hoja_svg, dir_pngs, hoja_png_name)
#     unesvg_png(hoja_png, hoja_datos_variables_svg, temp_final, "svg" + str(hoja) + ".svg")
#     # prepara_svg_para_pdf2(path_svg_entrada, path_svg_salida, name_svg, cartones_png,testigo=False)
#
#     tira1 = tira1 + 1
#     tira2 = tira2 + 1
#     carton_id = carton_id + 6
#     carton_id2 = carton_id2 + 6
#     if page == hojas_por_pdf:
#         pdf_file_name = "bingo" + completa_numero(5, pdf) + ".pdf"
#         multi_svgs_a_1_pdf(pdf_file_name, salida_dir, temp_final)
#         pdf = pdf + 1
#         temp_final = crear_carpeta("carpeta_svgsfinal" + completa_numero(5, pdf), salida_dir)
#         page = 0
#         print("Preparandos PDFS", " desde ", str(copy.copy(tira1)), " hasta ", str(copy.copy(tira1) + 100))
# pdf_file_name = "bingo" + completa_numero(5, pdf) + ".pdf"
# multi_svgs_a_1_pdf(pdf_file_name, salida_dir, temp_final)
#
# print("--------------")
# print(len(lista_hojas))
# print("--------------")
#
# print("fusionado")
