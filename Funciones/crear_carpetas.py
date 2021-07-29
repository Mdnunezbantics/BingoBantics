import os

def crear_carpeta(dir_name, path):
    name = str(dir_name)
    if name not in os.listdir(path):
        os.mkdir(os.path.join(path, name))
        # print("se crea carpeta", name)
    return os.path.join(path, name)
