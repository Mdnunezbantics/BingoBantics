import copy
import shutil
from pathlib import Path
import os
from Funciones.crear_carpetas import crear_carpeta
from Funciones.modifica_svg import prepara_carton_svg, svgtopng, prepara_carton_svg2, prepara_hoja_carton, \
    multi_svgs_a_1_pdf
from Funciones.numerador import generar_carton, generar_plancha, generar_hoja_carton, generar_hoja_carton2
from Funciones.varios import saca_x, completa_numero

salida = "output"
svg_base = "Carton_base.svg"
hoja_carton_base = "Hoja_carton_base.svg"
png_vacio = "vacio.png"
base_dir = Path(__file__).resolve().parent
if salida in os.listdir(base_dir):
    print("se encotro carpeta la eliminaremos")
    shutil.rmtree(os.path.join(base_dir, salida))

salida_dir = crear_carpeta(salida, base_dir)
bases = os.path.join(base_dir, "svgs")
carton_svg = os.path.join(bases, svg_base)
vaciopng_path = os.path.join(bases, png_vacio)


rec_vacio = os.path.join(bases, "rect_vacio.svg")

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
print("generamos cartones")
for page in range(cantidad_hojas):
    cartones_para_hoja = []
    # print(page)
    for x in range(2):
        # item = generar_hoja_carton()
        item = generar_hoja_carton2()
        while item in lista_hojas:
            # item = generar_hoja_carton()
            item = generar_hoja_carton2()
        cartones_para_hoja = cartones_para_hoja + item
        lista_hojas.append(item)
        # cartones_para_hoja.append(item)
    # print(item)
    lista_cartones.append(cartones_para_hoja)


hojas_por_pdf = 100
print("preparamos pdf")
pdf = 1
page = 0
tira1 = 1
tira2 = cantidad_hojas + 1
carton_id = 1
temp_svg = crear_carpeta("carpeta_svgs" + completa_numero(5, pdf), salida_dir)
png = svgtopng(rec_vacio, temp_svg, "vacio.png")
for hojita in lista_cartones:
    page = page + 1
    hoja = completa_numero(5, page)
    prepara_hoja_carton(hoja_base_svg, temp_svg, "%c", "%", "svg" + str(hoja) + ".svg", vaciopng_path, hojita, tira1,
                        tira2, carton_id)
    tira1 = tira1 + 1
    tira2 = tira2 + 1
    carton_id = carton_id + 12
    if page == hojas_por_pdf:
        pdf_file_name = "bingo" + completa_numero(5, pdf) + ".pdf"
        multi_svgs_a_1_pdf(pdf_file_name, salida_dir, temp_svg, png)
        pdf = pdf + 1
        temp_svg = crear_carpeta("carpeta_svgs" + completa_numero(5, pdf), salida_dir)
        png = svgtopng(rec_vacio, temp_svg, "vacio.png")
        page = 0
print(pdf)
pdf_file_name = "bingo" + completa_numero(5, pdf) + ".pdf"
multi_svgs_a_1_pdf(pdf_file_name, salida_dir, temp_svg, png)
# shutil.rmtree(temp_svg)


print("--------------")
print(len(lista_hojas))
print("--------------")

print("fusionado")












# temp_pdf = crear_carpeta("temp_pdf", salida_dir)
# list_svg_dir = os.listdir(temp_svg)
# file_list = []
# list_svg_dir.sort()
# for file in list_svg_dir:
#     if ".svg" in file:
#         file_svg = os.path.join(temp_svg, file)
#         file_pdf = os.path.join(temp_pdf, file[:-4] + ".pdf")
#         cairosvg.svg2pdf(file_obj=open(file_svg, "rb"), write_to=file_pdf)
#         # print(file)
#
#
# pdf_file_name = "bingo.pdf"
# pdf_output = os.path.join(salida_dir, pdf_file_name)
#
# merge.Merge(pdf_output).merge_folder(temp_pdf)
#

