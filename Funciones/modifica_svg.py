import shutil
from merge_pdf import merge
import ntpath
from xml.dom import minidom
import os
import codecs
import cairosvg
from pdftopng import pdftopng
import datos_variables
from Funciones.crear_carpetas import crear_carpeta
from Funciones.varios import completa_numero


def svgtopng(path_svg, path_png, png_name):
    file_pdf = os.path.join(path_png, png_name + ".pdf")
    file = os.path.join(path_png, png_name)
    file_png = file + ".png"
    cairosvg.svg2pdf(file_obj=open(path_svg, "rb"), write_to=file_pdf)
    pdftopng.convert(pdf_path=file_pdf, png_path=file)
    os.remove(file_pdf)

    return file_png


def prepara_hoja_carton(path_svg_entrada, path_svg_salida, ini_variable, fin_variable,
                        name_svg, png_path, list_carton, tira1, tira2, carton_id, carton_id2):
    xmldoc = minidom.parse(path_svg_entrada)
    id_carton = 0
    for carton in list_carton:
        id_carton = id_carton + 1
        dato = 0
        for num in carton:
            dato = dato + 1
            variable = str(ini_variable) + str(id_carton) + "b" + str(dato) + str(fin_variable)
            image_id = "imagec" + str(id_carton) + "b-" + str(dato)
            if num != "X":
                for text in xmldoc.getElementsByTagName('text'):
                    for tspan in text.getElementsByTagName('tspan'):
                        try:
                            if str(variable) in tspan.firstChild.wholeText:
                                tspan.firstChild.replaceWholeText(
                                    str(tspan.firstChild.wholeText).replace(str(variable), str(num)))
                        except Exception as e:
                            pass
                try:
                    for image in xmldoc.getElementsByTagName('image'):
                        if image.getAttribute('id') == str(image_id):
                            # print("se encontro variable")
                            parent = image.parentNode
                            parent.removeChild(image)
                except Exception as e:
                    pass
            else:
                for text in xmldoc.getElementsByTagName('text'):
                    for tspan in text.getElementsByTagName('tspan'):
                        try:
                            if str(variable) in tspan.firstChild.wholeText:
                                parent = tspan.parentNode
                                parent.removeChild(tspan)
                        except Exception as e:
                            pass
                for image in xmldoc.getElementsByTagName('image'):
                    if image.getAttribute('id') == str(image_id):
                        image.removeAttribute('sodipodi:absref')
                        image.removeAttribute('xlink:href')
                        image.setAttribute('sodipodi:absref', png_path[:-4])
                        image.setAttribute('xlink:href', png_path[:-4])
    d_fijos = {
        "%var_tira1%": completa_numero(4, tira1),
        "%var_tira2%": completa_numero(4, tira2),
        "%carton1%": completa_numero(5, carton_id),
        "%carton2%": completa_numero(5, carton_id + 1),
        "%carton3%": completa_numero(5, carton_id + 2),
        "%carton4%": completa_numero(5, carton_id + 3),
        "%carton5%": completa_numero(5, carton_id + 4),
        "%carton6%": completa_numero(5, carton_id + 5),

        "%carton7%": completa_numero(5, carton_id2 ),
        "%carton8%": completa_numero(5, carton_id2 + 1),
        "%carton9%": completa_numero(5, carton_id2 + 2),
        "%carton10%": completa_numero(5, carton_id2 + 3),
        "%carton11%": completa_numero(5, carton_id2 + 4),
        "%carton12%": completa_numero(5, carton_id2 + 5),
    }
    for var in d_fijos:
        for text in xmldoc.getElementsByTagName('text'):
            for tspan in text.getElementsByTagName('tspan'):
                try:
                    if str(var) in tspan.firstChild.wholeText:
                        tspan.firstChild.replaceWholeText(
                            str(tspan.firstChild.wholeText).replace(str(var), str(d_fijos.get(var))))
                except Exception as e:
                    pass
    new_svg_file = os.path.join(path_svg_salida, name_svg)
    with codecs.open(new_svg_file, "w", "utf-8") as out:
        xmldoc.writexml(out)
    return new_svg_file


def prepara_svg_para_pdf(path_svg_entrada, path_svg_salida, name_svg, testigo=False):
    xmldoc = minidom.parse(path_svg_entrada)
    var_testigo = "%TESTIGO%"
    d_variables = {
        "%var_cliente%": datos_variables.cliente,
        "%evento%": datos_variables.evento,
        "%var1%": datos_variables.bingo,
        "%var2%": datos_variables.linea,
        "%var3%": datos_variables.dos_linea,
        "%var4%": datos_variables.premios1,
        "%var5%": datos_variables.premios2,
        "%var6%": datos_variables.premios3,
        "%var7%": datos_variables.valor,
        "%serie%": datos_variables.serie,
        "%fecha%": datos_variables.fecha,
    }
    if not testigo:
        for var in d_variables:
            for text in xmldoc.getElementsByTagName('text'):
                for tspan in text.getElementsByTagName('tspan'):
                    try:
                        if str(var) in tspan.firstChild.wholeText:
                            tspan.firstChild.replaceWholeText(
                                str(tspan.firstChild.wholeText).replace(str(var), str(d_variables.get(var))))
                    except Exception as e:
                        pass
                    try:
                        if str(var_testigo) in tspan.firstChild.wholeText:
                            parent = tspan.parentNode
                            parent.removeChild(tspan)
                    except Exception as e:
                        pass
    if testigo:
        for var in d_variables:
            for text in xmldoc.getElementsByTagName('text'):
                for tspan in text.getElementsByTagName('tspan'):
                    if var != "%var_cliente%":
                        try:
                            if str(var) in tspan.firstChild.wholeText:
                                parent = tspan.parentNode
                                parent.removeChild(tspan)
                        except Exception as e:
                            pass
                    if var == "%var_cliente%":
                        try:
                            if str(var) in tspan.firstChild.wholeText:
                                tspan.firstChild.replaceWholeText(
                                    str(tspan.firstChild.wholeText).replace(str(var), str(d_variables.get(var))))
                        except Exception as e:
                            pass

                    try:
                        if str(var_testigo) in tspan.firstChild.wholeText:
                            tspan.firstChild.replaceWholeText(
                                str(tspan.firstChild.wholeText).replace(str(var_testigo), str("TESTIGO")))
                    except Exception as e:
                        pass
    new_svg_file = os.path.join(path_svg_salida, name_svg)
    with codecs.open(new_svg_file, "w", "utf-8") as out:
        xmldoc.writexml(out)
    return new_svg_file


def multi_svgs_a_1_pdf(pdf_file_name, output_path, svgs_dir):

    temp_pdf = crear_carpeta("temp_pdf", output_path)
    temp_svg_original = crear_carpeta("temp_svg_original", output_path)
    pdfs_originales = crear_carpeta("pdfs_originales", output_path)
    list_svg_dir = os.listdir(svgs_dir)
    list_svg_dir.sort()

    for file in list_svg_dir:
        if ".svg" in file:
            file_svg = os.path.join(svgs_dir, file)
            name_svg = "temp_" + ntpath.basename(file_svg)
            file_pdf = os.path.join(temp_pdf, file[:-4] + ".pdf")
            new_file_svg = prepara_svg_para_pdf(file_svg, temp_svg_original, name_svg, testigo=False)
            cairosvg.svg2pdf(file_obj=open(new_file_svg, "rb"), write_to=file_pdf)
    pdf_output = os.path.join(pdfs_originales, "originales_" + pdf_file_name)
    merge.Merge(pdf_output).merge_folder(temp_pdf)
    shutil.rmtree(temp_pdf)

    temp_pdf = crear_carpeta("temp_pdf", output_path)
    temp_svg_testigo = crear_carpeta("temp_svg_testigo", output_path)
    pdfs_testigo = crear_carpeta("pdfs_testigo", output_path)

    list_news_svg_dir = os.listdir(temp_svg_testigo)
    list_news_svg_dir.sort()

    for file in list_svg_dir:
        if ".svg" in file:
            file_svg = os.path.join(svgs_dir, file)
            name_svg = "temp_" + ntpath.basename(file_svg)
            file_pdf = os.path.join(temp_pdf, file[:-4] + ".pdf")
            new_file_svg = prepara_svg_para_pdf(file_svg, temp_svg_testigo, name_svg, testigo=True)
            cairosvg.svg2pdf(file_obj=open(new_file_svg, "rb"), write_to=file_pdf)

    pdf_output = os.path.join(pdfs_testigo, "testigos_" + pdf_file_name)

    merge.Merge(pdf_output).merge_folder(temp_pdf)

    shutil.rmtree(temp_pdf)
    shutil.rmtree(temp_svg_original)
    shutil.rmtree(temp_svg_testigo)
    return pdf_output


def unesvg_png(path_png, svg_base,  dir_output, name_svg):
    xmldoc = minidom.parse(svg_base)
    for image in xmldoc.getElementsByTagName('image'):
        if image.getAttribute('id') == str("cartones"):
            image.removeAttribute('sodipodi:absref')
            image.removeAttribute('xlink:href')
            image.setAttribute('sodipodi:absref', path_png)
            image.setAttribute('xlink:href', path_png)

    new_svg_file = os.path.join(dir_output, name_svg)
    with codecs.open(new_svg_file, "w", "utf-8") as out:
        xmldoc.writexml(out)
    return new_svg_file


