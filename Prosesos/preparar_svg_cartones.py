import os
import datos_variables
from Funciones.crear_carpetas import crear_carpeta
from Funciones.modifica_svg import svgtopng, unesvg_png, prepara_hoja_carton, prepara_hoja_carton1, prepara_hoja_carton2
from Funciones.varios import completa_numero


def preparar_png_cartones(base_dir, salida_dir, hojas, lista_cartones):

    cantidad_hojas = int(hojas)

    hoja_base_12_cartones = datos_variables.hoja_base_12_cartones
    png_vacio = datos_variables.png_vacio
    bases = os.path.join(base_dir, datos_variables.bases_svg)
    rec_vacio = os.path.join(bases, "rect_vacio.svg")
    hoja_base_12_cartones_svg = os.path.join(bases, hoja_base_12_cartones)
    hoja_base_6_cartones_svg = os.path.join(bases, "Hoja_base_6_cartones.svg")
    page = 0
    tira1 = 0
    tira2 = cantidad_hojas
    carton_id = 1
    carton_id2 = (cantidad_hojas * 6) + 1
    dir_svg_cartones = crear_carpeta("carpeta_svg_cartones", salida_dir)
    dir_pngs = crear_carpeta(datos_variables.dir_png, salida_dir)
    png = svgtopng(rec_vacio, bases, png_vacio)
    for hoja_carton in lista_cartones:

        page = page + 1
        hoja = completa_numero(5, page)
        name_carton_svg = "svg" + str(hoja) + ".svg"
        name_carton_svg1 = "svg" + str(completa_numero(4, tira1)) + ".svg"
        name_carton_svg2 = "svg" + str(completa_numero(4, tira2)) + ".svg"
        name_carton_png = "png" + str(hoja) + ".png"
        name_carton_png1 = "png" + str(completa_numero(4, tira1)) + ".png"
        name_carton_png2 = "png" + str(completa_numero(4, tira2)) + ".png"

        cart_1 = hoja_carton[:6]
        cart_2 = hoja_carton[6:]
        # print(cart_1)
        # print("----")
        # print(cart_2)


        # print(len(hoja_carton))
        # print(len(hoja_carton[0]))
        # print(len(hoja_carton[7]))
        hoja_carton_svg1 = prepara_hoja_carton1(hoja_base_6_cartones_svg, dir_svg_cartones, "%c", "%", name_carton_svg1,
                                              png, cart_1, tira1, tira2, carton_id, carton_id2)
        hoja_carton_svg2 = prepara_hoja_carton2(hoja_base_6_cartones_svg, dir_svg_cartones, "%c", "%", name_carton_svg2,
                                              png, cart_2, tira1, tira2, carton_id, carton_id2)

        # hoja_carton_svg = prepara_hoja_carton(hoja_base_12_cartones_svg, dir_svg_cartones,"%c", "%", name_carton_svg, png, hoja_carton,
        #                                       tira1, tira2, carton_id, carton_id2)
        # hoja_carton_png = svgtopng(hoja_carton_svg, dir_pngs, name_carton_png)
        hoja_carton_png1 = svgtopng(hoja_carton_svg1, dir_pngs, name_carton_png1)
        hoja_carton_png2 = svgtopng(hoja_carton_svg2, dir_pngs, name_carton_png2)
        tira1 = tira1 + 1
        tira2 = tira2 + 1
        carton_id = carton_id + 6
        carton_id2 = carton_id2 + 6
        print("Hoja Carton_base " + str(page))

    # print("--------------")
    # print(len(lista_cartones) * 6)
    # print("--------------")



