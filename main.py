import pickle
import datetime

import slugify as slugify
import datos_variables
from Funciones.crear_carpetas import crear_carpeta
from Prosesos.crear_lista_cartones import crear_lista_cartones
from Prosesos.crear_pdf import hacer_pdfs
from Prosesos.preparar_svg_cartones import preparar_png_cartones
from pathlib import Path
import os
import shutil
from slugify import slugify

fecha = str(datetime.date.today()).split("-")
fecha = str(fecha[2]) + "-" + str(fecha[1]) + "-" + str(fecha[0])
print(fecha)
hora = datetime.datetime.now()
hora = str(hora.hour) + ":" + str(hora.minute) + ":" + str(hora.second)
print(hora)
salida = datos_variables.salida
base_dir = Path(__file__).resolve().parent
pickle_dir = crear_carpeta("Pickle", base_dir)

preparar_lista = input("preparar nuevamente la lista si/no ")
lista_cartones = []
hojas = 0
class ObjetoCartones:
    cantidad_de_hojas = 0
    lista_cartones = []

if preparar_lista == "si":
    hojas = input("indique la cantidad de hojas a realizar ")
    objeto_cartones = ObjetoCartones()

    file_cartones = open(os.path.join(pickle_dir, 'pickle-' + str(fecha) + "-" + slugify(datos_variables.cliente)), 'wb')
    lista_cartones = crear_lista_cartones(int(hojas))
    objeto_cartones.cantidad_de_hojas = int(hojas)
    objeto_cartones.lista_cartones = lista_cartones

    pickle.dump(objeto_cartones, file_cartones)
    file_cartones.close()

if preparar_lista == "no":
    pickle_file_name = 'pickle-' + str(fecha) + "-" + slugify(datos_variables.cliente)
    if pickle_file_name in os.listdir(pickle_dir):
        file_cartones = open(os.path.join(pickle_dir, pickle_file_name), 'rb')
        objeto_cartones = pickle.load(file_cartones)
        lista_cartones = objeto_cartones.lista_cartones
        hojas = int(objeto_cartones.cantidad_de_hojas)
        file_cartones.close()
    else:
        print("Pickle File no encontrado")
        pickle_file_name = input("especifique pickle file name ")
        file_cartones = open(os.path.join(pickle_dir, str(pickle_file_name)), 'rb')
        objeto_cartones = pickle.load(file_cartones)
        lista_cartones = objeto_cartones.lista_cartones
        hojas = objeto_cartones.cantidad_de_hojas
        file_cartones.close()
hora = datetime.datetime.now()
hora = str(hora.hour) + ":" + str(hora.minute) + ":" + str(hora.second)
print(hora)

print("se realizaran " + str(hojas) + " hojas siendo " + str(int(hojas) * 12) + " cartones")

trabajo_completo = input("Realizar el trabajo completo (si/no): ")
if trabajo_completo == "si":
    testigo = input("Realizar el testigo (si/no): ")
    if salida in os.listdir(base_dir):
        print("Se encotro carpeta la eliminaremos")
        shutil.rmtree(os.path.join(base_dir, salida))
    print("Se crea carpeta output")
    salida_dir = crear_carpeta(salida, base_dir)

    print("Inicio proseso 1")
    preparar_png_cartones(base_dir, salida_dir, hojas, lista_cartones)
    print("Fin proseso 1")
    hora = datetime.datetime.now()
    hora = str(hora.hour) + ":" + str(hora.minute) + ":" + str(hora.second)
    print(hora)
    if testigo == "si":
        print("Inicio proseso 2")
        hacer_pdfs(base_dir, "pdfs", "bingo", preparar_testigo=True)
        print("Fin proseso 2")
        hora = datetime.datetime.now()
        hora = str(hora.hour) + ":" + str(hora.minute) + ":" + str(hora.second)
        print(hora)
    else:
        print("Inicio proseso 2")
        hacer_pdfs(base_dir, "pdfs", "bingo", preparar_testigo=False)
        print("Fin proseso 2")
        hora = datetime.datetime.now()
        hora = str(hora.hour) + ":" + str(hora.minute) + ":" + str(hora.second)
        print(hora)

if trabajo_completo == "no":
    generar_pdf = input("Generar los pdf (si/no): ")
    if generar_pdf == "si":
        hacer_pdfs(base_dir, "pdfs", "bingo", preparar_testigo=True)
        hora = datetime.datetime.now()
        hora = str(hora.hour) + ":" + str(hora.minute) + ":" + str(hora.second)
        print(hora)