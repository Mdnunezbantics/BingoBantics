import datos_variables
from Funciones.crear_carpetas import crear_carpeta
from Prosesos.crear_pdf import hacer_pdfs
from Prosesos.preparar_svg_cartones import preparar_png_cartones
from pathlib import Path
import os
import shutil



salida = datos_variables.salida

base_dir = Path(__file__).resolve().parent
trabajo_completo = input("escriba si para realizar el trabajo completo")
print(trabajo_completo)
if trabajo_completo == "si":

    if salida in os.listdir(base_dir):
        print("se encotro carpeta la eliminaremos")
        shutil.rmtree(os.path.join(base_dir, salida))
    print("se crea carpeta output")
    salida_dir = crear_carpeta(salida, base_dir)

    print("inicio")
    preparar_png_cartones(base_dir, salida_dir)
    print("fin")

    print("inicio")
    hacer_pdfs(base_dir, "pdfs", "bingo")
    print("inicio")

else:
    generar_pdf = input("escriba si para generar los pdf")
    if generar_pdf == "si":
        hacer_pdfs(base_dir, "pdfs", "bingo")