import copy
import shutil
from pathlib import Path
import os
from Funciones.crear_carpetas import crear_carpeta
from Funciones.modifica_svg import svgtopng, prepara_hoja_carton, multi_svgs_a_1_pdf
from Funciones.numerador import generar_hoja_carton
from Funciones.varios import completa_numero

crear_pdf = True
cantidad_hojas = 5000
hojas_por_pdf = 100

salida = "output"
svg_base = "Carton_base.svg"
hoja_carton_base = "Hoja_carton_base.svg"
png_vacio = "vacio.png"

base_dir = Path(__file__).resolve().parent
if salida in os.listdir(base_dir):
    print("se encotro carpeta la eliminaremos")
    shutil.rmtree(os.path.join(base_dir, salida))
print("se crea carpeta output")
salida_dir = crear_carpeta(salida, base_dir)
bases = os.path.join(base_dir, "svgs")
rec_vacio = os.path.join(bases, "rect_vacio.svg")
hoja_base_svg = os.path.join(bases, hoja_carton_base)

if crear_pdf:
    print("Generamos cartones")
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
    print("Cartones Listos")
    print("Preparamos PDFS")
    pdf = 1
    page = 0
    tira1 = 0
    tira2 = cantidad_hojas
    carton_id = 1
    carton_id2 = (cantidad_hojas * 6) + 1
    print("Se crea carpeta_svgs" + completa_numero(5, pdf))
    temp_svg = crear_carpeta("carpeta_svgs" + completa_numero(5, pdf), salida_dir)
    png = svgtopng(rec_vacio, temp_svg, png_vacio)
    print("Preparandos PDFS", " desde ", str(copy.copy(tira1)), " hasta ", str(copy.copy(tira1) + 100))
    for hoja_carton in lista_cartones:
        page = page + 1
        hoja = completa_numero(5, page)
        prepara_hoja_carton(hoja_base_svg, temp_svg, "%c", "%", "svg" + str(hoja) + ".svg", png, hoja_carton, tira1,
                            tira2, carton_id, carton_id2)
        tira1 = tira1 + 1
        tira2 = tira2 + 1
        carton_id = carton_id + 6
        carton_id2 = carton_id2 + 6
        if page == hojas_por_pdf:

            pdf_file_name = "bingo" + completa_numero(5, pdf) + ".pdf"
            multi_svgs_a_1_pdf(pdf_file_name, salida_dir, temp_svg, png)
            pdf = pdf + 1
            temp_svg = crear_carpeta("carpeta_svgs" + completa_numero(5, pdf), salida_dir)
            png = svgtopng(rec_vacio, temp_svg, png_vacio)
            page = 0
            print("Preparandos PDFS", " desde ", str(copy.copy(tira1)), " hasta ", str(copy.copy(tira1) + 100))
    pdf_file_name = "bingo" + completa_numero(5, pdf) + ".pdf"
    multi_svgs_a_1_pdf(pdf_file_name, salida_dir, temp_svg, png)

    print("--------------")
    print(len(lista_hojas))
    print("--------------")

    print("fusionado")
