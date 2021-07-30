import os
import shutil
import copy
from pathlib import Path

import datos_variables
from Funciones.crear_carpetas import crear_carpeta
from Funciones.modifica_svg import multi_svgs_a_1_pdf
from Funciones.varios import completa_numero


def hacer_pdfs():
    base_dir = Path(__file__).resolve().parent
    salida_dir = os.path.join(base_dir, datos_variables.salida)

    output_path = crear_carpeta(datos_variables.carpeta_fianal_name, salida_dir)

    dir_hojas_completas = os.path.join(base_dir, datos_variables.salida, datos_variables.carpeta_fianal_name)
    pdf = 1
    svg_list = os.listdir(dir_hojas_completas)
    svg_list.sort()
    for file in svg_list:
        pdf = pdf + 1
        print(pdf)
        svg_file = os.path.join(dir_hojas_completas, str(file))
        print(svg_file)
        temp = crear_carpeta("temp", salida_dir)
        shutil.copy(svg_file, os.path.join(temp, str(file)))
        pdf_file_name = "bingo" + completa_numero(5, pdf) + ".pdf"
        multi_svgs_a_1_pdf(pdf_file_name, output_path, temp)

