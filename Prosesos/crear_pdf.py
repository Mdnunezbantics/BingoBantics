import os
import shutil
import datos_variables
from Funciones.crear_carpetas import crear_carpeta
from Funciones.modifica_svg import multi_svgs_a_1_pdf, unesvg_png
from Funciones.varios import completa_numero


def hacer_pdfs(base_dir, salida_dir_name, pdfs_name, preparar_testigo=False):

    salida_dir = os.path.join(base_dir, datos_variables.salida)
    bases = os.path.join(base_dir, datos_variables.bases_svg)
    hoja_datos_variables = datos_variables.hoja_datos_variables
    hoja_datos_variables_svg = os.path.join(bases, hoja_datos_variables)
    hoja_datos_variables_svg2 = os.path.join(bases, "Hoja_datos_variables2.svg")
    dir_hojas_completas = crear_carpeta(datos_variables.carpeta_fianal_name, salida_dir)
    dir_png = os.path.join(salida_dir, datos_variables.dir_png)

    png_list = os.listdir(dir_png)
    png_list.sort()
    archivo = 1
    list_files = []

    print(len(png_list))
    print((len(png_list) // 2))
    for file in png_list:
        list_files.append(str(file))
        print(len(list_files))
        if len(list_files) == 500:
            print("iiiiiiiiiiiiiiiii")
            for item in range(len(list_files)//2):
                png_path = os.path.join(dir_png, str(list_files[int(item)]))
                png_path2 = os.path.join(dir_png, str(list_files[int(item) + (len(list_files)//2)]))
                print(archivo)
                name_hoja_svg = "svg" + completa_numero(5, archivo) + ".svg"
                hoja_completa = unesvg_png(png_path, png_path2, hoja_datos_variables_svg2, dir_hojas_completas, name_hoja_svg)
                print("Hoja Carton " + str(archivo))
                archivo = archivo + 1
            list_files = []
    print("sssss")
    print(len(list_files))
    print(list_files)
    if len(list_files) <= 500:
        for item in range(len(list_files)//2):
            png_path = os.path.join(dir_png, str(list_files[int(item)]))
            png_path2 = os.path.join(dir_png, str(list_files[int(item) + (len(list_files)//2)]))
            print(archivo)
            name_hoja_svg = "svg" + completa_numero(5, archivo) + ".svg"
            hoja_completa = unesvg_png(png_path, png_path2, hoja_datos_variables_svg2, dir_hojas_completas,
                                       name_hoja_svg)
            print("Hoja Carton " + str(archivo))
            archivo = archivo + 1


    # for file in png_list:
    #     png_path = os.path.join(dir_png, str(file))
    #     name_hoja_svg = "svg" + completa_numero(5, archivo) + ".svg"
    #     hoja_completa = unesvg_png(png_path, hoja_datos_variables_svg, dir_hojas_completas, name_hoja_svg)
    #     print("Hoja Carton " + str(archivo))
    #     archivo = archivo + 1

    svg_list = os.listdir(dir_hojas_completas)
    svg_list.sort()
    print("Preparamos PDFS")
    if salida_dir_name in os.listdir(salida_dir):
        shutil.rmtree(os.path.join(salida_dir, salida_dir_name))

    if preparar_testigo:
        output_dir = crear_carpeta(salida_dir_name, salida_dir)
        temp_svg = crear_carpeta("temp_svg", output_dir)
        hoja = 0
        pdf = 1
        for svg in svg_list:
            svg_path = os.path.join(dir_hojas_completas, str(svg))
            shutil.copy(svg_path, temp_svg)
            hoja = hoja + 1
            if hoja == datos_variables.hojas_por_pdf:
                print("Preparamos PDF: hasta la hoja:", str(pdf * 100))
                pdf_file_name = pdfs_name + completa_numero(5, pdf) + ".pdf"
                multi_svgs_a_1_pdf(pdf_file_name, output_dir, temp_svg, hacer_testigo=True)
                shutil.rmtree(temp_svg)
                temp_svg = crear_carpeta("temp_svg", output_dir)
                pdf = pdf + 1
                hoja = 0

        pdf_file_name = pdfs_name + completa_numero(5, pdf) + ".pdf"
        multi_svgs_a_1_pdf(pdf_file_name, output_dir, temp_svg)
        shutil.rmtree(temp_svg)



