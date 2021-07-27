import ntpath
from xml.dom import minidom
import os
import codecs
from pathlib import Path
import cairosvg
from pdftopng import pdftopng
from Funciones.numerador import generar_carton


def modificar_label_en_svg(path_svg_entrada, path_svg_salida, name_svg_salida, var_name, var_modificar):
    print("d")
    # xmldoc = minidom.parse(path_svg_entrada)
    # path_base = path_svg_entrada.replace(ntpath.basename(path_svg_entrada), "")
    #
    # for text in xmldoc.getElementsByTagName('text'):
    #     for tspan in text.getElementsByTagName('tspan'):
    #         try:
    #             if str(var_name) in tspan.firstChild.wholeText:
    #                 tspan.firstChild.replaceWholeText(str(tspan.firstChild.wholeText).replace(str(var_name), str(var_modificar)))
    #                 # tspan.firstChild.replaceWholeText(str(var_modificar))
    #         except Exception as e:
    #             print(str(e))
    # new_svg_file = os.path.join(path_svg_salida, name_svg_salida)
    #
    # with codecs.open(new_svg_file, "w", "utf-8") as out:
    #     xmldoc.writexml(out)
    #
    # return new_svg_file


def prepara_carton_svg(path_svg_entrada, path_svg_salida, ini_variable, fin_variable, name_svg, png_path):
    xmldoc = minidom.parse(path_svg_entrada)
    num_carton = generar_carton()
    path_png = os.path.join(path_svg_salida, ntpath.basename(png_path))
    dato = 0
    print(num_carton)
    for num in num_carton:
        dato = dato + 1
        variable = str(ini_variable) + str(dato) + str(fin_variable)
        # print(variable)
        image_id = "vaciob" + str(dato)
        if num != "X":
            for text in xmldoc.getElementsByTagName('text'):
                for tspan in text.getElementsByTagName('tspan'):
                    try:
                        if str(variable) in tspan.firstChild.wholeText:
                            tspan.firstChild.replaceWholeText(
                                str(tspan.firstChild.wholeText).replace(str(variable), str(num)))
                    except Exception as e:
                        # print(str(e))
                        pass
            try:
                for image in xmldoc.getElementsByTagName('image'):
                    if image.getAttribute('id') == str(image_id):
                        # print("se encontro variable")
                        parent = image.parentNode
                        parent.removeChild(image)
            except Exception as e:
                # print(str(e))
                pass
        else:
            for text in xmldoc.getElementsByTagName('text'):
                for tspan in text.getElementsByTagName('tspan'):
                    try:
                        if str(variable) in tspan.firstChild.wholeText:
                            parent = tspan.parentNode
                            parent.removeChild(tspan)
                    except Exception as e:
                        # print(str(e))
                        pass

            for image in xmldoc.getElementsByTagName('image'):
                if image.getAttribute('id') == str(image_id):
                    # image.removeAttribute('xlink:href')
                    image.removeAttribute('sodipodi:absref')
                    image.setAttribute('sodipodi:absref', path_png)
                    # image.setAttribute('xlink:href', str(png_url))

    new_svg_file = os.path.join(path_svg_salida, name_svg)

    with codecs.open(new_svg_file, "w", "utf-8") as out:
        xmldoc.writexml(out)

    return new_svg_file


def svgtopng(path_svg, path_png, png_name):
    file_pdf = os.path.join(path_png, png_name + ".pdf")
    file = os.path.join(path_png, png_name)
    file_png = file + ".png"
    cairosvg.svg2pdf(file_obj=open(path_svg, "rb"), write_to=file_pdf)
    pdftopng.convert(pdf_path=file_pdf, png_path=file)
    os.remove(file_pdf)

    return file_png


def prepara_carton_svg2(path_svg_entrada, path_svg_salida, ini_variable, fin_variable, name_svg, png_path, num_carton):
    xmldoc = minidom.parse(path_svg_entrada)
    path_png = os.path.join(path_svg_salida, ntpath.basename(png_path))
    dato = 0
    for num in num_carton:
        dato = dato + 1
        variable = str(ini_variable) + str(dato) + str(fin_variable)
        # print(variable)
        image_id = "vaciob" + str(dato)
        if num != "X":
            for text in xmldoc.getElementsByTagName('text'):
                for tspan in text.getElementsByTagName('tspan'):
                    try:
                        if str(variable) in tspan.firstChild.wholeText:
                            tspan.firstChild.replaceWholeText(
                                str(tspan.firstChild.wholeText).replace(str(variable), str(num)))
                    except Exception as e:
                        # print(str(e))
                        pass
            try:
                for image in xmldoc.getElementsByTagName('image'):
                    if image.getAttribute('id') == str(image_id):
                        # print("se encontro variable")
                        parent = image.parentNode
                        parent.removeChild(image)
            except Exception as e:
                # print(str(e))
                pass
        else:
            for text in xmldoc.getElementsByTagName('text'):
                for tspan in text.getElementsByTagName('tspan'):
                    try:
                        if str(variable) in tspan.firstChild.wholeText:
                            parent = tspan.parentNode
                            parent.removeChild(tspan)
                    except Exception as e:
                        # print(str(e))
                        pass

            for image in xmldoc.getElementsByTagName('image'):
                if image.getAttribute('id') == str(image_id):
                    # image.removeAttribute('xlink:href')
                    image.removeAttribute('sodipodi:absref')
                    image.setAttribute('sodipodi:absref', path_png)
                    # image.setAttribute('xlink:href', str(png_url))

    new_svg_file = os.path.join(path_svg_salida, name_svg)

    with codecs.open(new_svg_file, "w", "utf-8") as out:
        xmldoc.writexml(out)

    return new_svg_file


def prepara_hoja_carton(path_svg_entrada, path_svg_salida, ini_variable, fin_variable, name_svg, png_path, list_carton):
    xmldoc = minidom.parse(path_svg_entrada)
    path_png = os.path.join(path_svg_salida, ntpath.basename(png_path))
    dato = 0
    id_carton = 0

    for carton in list_carton:
        id_carton = id_carton + 1
        dato = 0
        # print(id_carton)
        for num in carton:
            dato = dato + 1
            variable = str(ini_variable) + str(id_carton) + "b" + str(dato) + str(fin_variable)
            # print(variable)
            image_id = "imagec" + str(id_carton) + "b-" + str(dato)
            if num != "X":
                for text in xmldoc.getElementsByTagName('text'):
                    for tspan in text.getElementsByTagName('tspan'):
                        try:
                            if str(variable) in tspan.firstChild.wholeText:
                                tspan.firstChild.replaceWholeText(
                                    str(tspan.firstChild.wholeText).replace(str(variable), str(num)))
                        except Exception as e:
                            # print(str(e))
                            pass
                try:
                    for image in xmldoc.getElementsByTagName('image'):
                        if image.getAttribute('id') == str(image_id):
                            # print("se encontro variable")
                            parent = image.parentNode
                            parent.removeChild(image)
                except Exception as e:
                    # print(str(e))
                    pass
            else:
                for text in xmldoc.getElementsByTagName('text'):
                    for tspan in text.getElementsByTagName('tspan'):
                        try:
                            if str(variable) in tspan.firstChild.wholeText:
                                parent = tspan.parentNode
                                parent.removeChild(tspan)
                        except Exception as e:
                            # print(str(e))
                            pass

                for image in xmldoc.getElementsByTagName('image'):
                    if image.getAttribute('id') == str(image_id):
                        # image.removeAttribute('xlink:href')
                        image.removeAttribute('sodipodi:absref')
                        image.setAttribute('sodipodi:absref', path_png)
                        # image.setAttribute('xlink:href', str(png_url))

    new_svg_file = os.path.join(path_svg_salida, name_svg)

    with codecs.open(new_svg_file, "w", "utf-8") as out:
        xmldoc.writexml(out)

    return new_svg_file