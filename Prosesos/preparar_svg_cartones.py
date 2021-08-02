import os
import copy
import datos_variables
from Funciones.crear_carpetas import crear_carpeta
from Funciones.modifica_svg import svgtopng, unesvg_png, prepara_hoja_carton
from Funciones.varios import completa_numero
from Prosesos.crear_lista_cartones import crear_lista_cartones


def preparar_png_cartones(base_dir, salida_dir, hojas):

    cantidad_hojas = int(hojas)
    lista_cartones, lista_hojas = crear_lista_cartones(cantidad_hojas)
    hoja_base_12_cartones = datos_variables.hoja_base_12_cartones
    png_vacio = datos_variables.png_vacio
    bases = os.path.join(base_dir, datos_variables.bases_svg)
    rec_vacio = os.path.join(bases, "rect_vacio.svg")
    hoja_base_12_cartones_svg = os.path.join(bases, hoja_base_12_cartones)

    page = 0
    tira1 = 0
    tira2 = cantidad_hojas
    carton_id = 1
    carton_id2 = (cantidad_hojas * 6) + 1
    dir_svg_cartones = crear_carpeta("carpeta_svg_cartones", salida_dir)
    dir_pngs = crear_carpeta(datos_variables.dir_png, salida_dir)

    png = svgtopng(rec_vacio, bases, png_vacio)

    for hoja_carton in lista_cartones:
        print(page)
        page = page + 1
        hoja = completa_numero(5, page)
        name_carton_svg = "svg" + str(hoja) + ".svg"
        name_carton_png = "png" + str(hoja) + ".png"

        hoja_carton_svg = prepara_hoja_carton(hoja_base_12_cartones_svg, dir_svg_cartones,"%c", "%", name_carton_svg, png, hoja_carton,
                                              tira1, tira2, carton_id, carton_id2)
        hoja_carton_png = svgtopng(hoja_carton_svg, dir_pngs, name_carton_png)
        tira1 = tira1 + 1
        tira2 = tira2 + 1
        carton_id = carton_id + 6
        carton_id2 = carton_id2 + 6

    print("--------------")
    print(len(lista_hojas))
    print("--------------")



