import os
import shutil
import copy
import datos_variables
from pathlib import Path
from Funciones.crear_carpetas import crear_carpeta
from Funciones.modifica_svg import svgtopng, unesvg_png, prepara_hoja_carton, multi_svgs_a_1_pdf
from Funciones.varios import completa_numero
from crear_lista_cartones import crear_lista_cartones
from crear_pdf import hacer_pdfs


def trabajo_completo():
    base_dir = Path(__file__).resolve().parent
    cantidad_hojas = datos_variables.cantidad_hojas
    hojas_por_pdf = datos_variables.hojas_por_pdf
    lista_cartones, lista_hojas = crear_lista_cartones(cantidad_hojas)
    salida = datos_variables.salida
    svg_base = datos_variables.svg_base
    hoja_carton_base = datos_variables.hoja_carton_base
    hoja_datos_variables = datos_variables.hoja_datos_variables
    hoja_base_12_cartones = datos_variables.hoja_base_12_cartones
    png_vacio = datos_variables.png_vacio

    if salida in os.listdir(base_dir):
        print("se encotro carpeta la eliminaremos")
        shutil.rmtree(os.path.join(base_dir, salida))
    print("se crea carpeta output")
    salida_dir = crear_carpeta(salida, base_dir)
    bases = os.path.join(base_dir, "svgs")
    rec_vacio = os.path.join(bases, "rect_vacio.svg")
    hoja_base_svg = os.path.join(bases, hoja_carton_base)

    hoja_datos_variables_svg = os.path.join(bases, hoja_datos_variables)
    hoja_base_12_cartones_svg = os.path.join(bases, hoja_base_12_cartones)



    print("Preparamos PDFS")
    pdf = 1
    page = 0
    tira1 = 0
    tira2 = cantidad_hojas
    carton_id = 1
    carton_id2 = (cantidad_hojas * 6) + 1
    print("Se crea carpeta_svgs" + completa_numero(5, pdf))

    dir_svg_cartones = crear_carpeta("carpeta_svg_cartones", salida_dir)
    dir_pngs = crear_carpeta("carpeta_pngs_cartones", salida_dir)
    dir_hojas_completas = crear_carpeta(datos_variables.carpeta_fianal_name, salida_dir)

    png = svgtopng(rec_vacio, bases, png_vacio)
    print("Preparandos PDFS", " desde ", str(copy.copy(tira1)), " hasta ", str(copy.copy(tira1) + 100))
    for hoja_carton in lista_cartones:
        print(page)
        page = page + 1
        hoja = completa_numero(5, page)
        name_carton_svg = "svg" + str(hoja) + ".svg"
        name_carton_png = "png" + str(hoja) + ".png"
        name_hoja_svg = "svg" + str(hoja) + ".svg"
        hoja_carton_svg = prepara_hoja_carton(hoja_base_12_cartones_svg, dir_svg_cartones,"%c", "%", name_carton_svg, png, hoja_carton,
                                              tira1, tira2, carton_id, carton_id2)

        hoja_carton_png = svgtopng(hoja_carton_svg, dir_pngs, name_carton_png)

        hoja_completa = unesvg_png(hoja_carton_png, hoja_datos_variables_svg, dir_hojas_completas, name_hoja_svg)

        tira1 = tira1 + 1
        tira2 = tira2 + 1
        carton_id = carton_id + 6
        carton_id2 = carton_id2 + 6

    print("--------------")
    print(len(lista_hojas))
    print("--------------")

    print("fusionado")
