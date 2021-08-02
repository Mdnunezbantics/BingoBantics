import os
import shutil
import datos_variables
from Funciones.crear_carpetas import crear_carpeta
from Funciones.modifica_svg import multi_svgs_a_1_pdf, unesvg_png
from Funciones.varios import completa_numero


def hacer_pdfs(base_dir, salida_dir_name, pdfs_name):

    salida_dir = os.path.join(base_dir, datos_variables.salida)
    bases = os.path.join(base_dir, datos_variables.bases_svg)
    hoja_datos_variables = datos_variables.hoja_datos_variables
    hoja_datos_variables_svg = os.path.join(bases, hoja_datos_variables)
    dir_hojas_completas = crear_carpeta(datos_variables.carpeta_fianal_name, salida_dir)
    dir_png = os.path.join(salida_dir, datos_variables.dir_png)

    png_list = os.listdir(dir_png)
    png_list.sort()
    archivo = 1
    for file in png_list:
        png_path = os.path.join(dir_png, str(file))
        name_hoja_svg = "svg" + completa_numero(5, archivo) + ".svg"
        hoja_completa = unesvg_png(png_path, hoja_datos_variables_svg, dir_hojas_completas, name_hoja_svg)
        print(archivo)
        archivo = archivo + 1

    svg_list = os.listdir(dir_hojas_completas)
    svg_list.sort()
    print("Preparamos PDFS")
    if salida_dir_name in os.listdir(salida_dir):
        shutil.rmtree(os.path.join(salida_dir, salida_dir_name))

    output_dir = crear_carpeta(salida_dir_name, salida_dir)
    temp_svg = crear_carpeta("temp_svg", output_dir)
    hoja = 0
    pdf = 1
    print(len(svg_list))
    for svg in svg_list:
        svg_path = os.path.join(dir_hojas_completas, str(svg))
        shutil.copy(svg_path, temp_svg)
        hoja = hoja + 1
        if hoja == datos_variables.hojas_por_pdf:
            print("Preparamos PDF: hasta", str(pdf * 100))
            pdf_file_name = pdfs_name + completa_numero(5, pdf) + ".pdf"
            multi_svgs_a_1_pdf(pdf_file_name, output_dir, temp_svg)
            shutil.rmtree(temp_svg)
            temp_svg = crear_carpeta("temp_svg", output_dir)
            pdf = pdf + 1
            hoja = 0

    pdf_file_name = pdfs_name + completa_numero(5, pdf) + ".pdf"
    multi_svgs_a_1_pdf(pdf_file_name, output_dir, temp_svg)
    shutil.rmtree(temp_svg)



