import pandas as pd
from openpyxl import load_workbook

archivo_uno = pd.read_excel('../archivos/INVENTARIO 31DIC.xlsx', sheet_name="Hoja2", header=0)
archivo_dos = pd.read_excel('../archivos/REPORTE DE MAQUINARIA PARA ALMACÉN_11  12-01-2024) (2).xlsx', sheet_name="Hoja1", header=9)

archivo_dos_path = '../archivos/REPORTE DE MAQUINARIA PARA ALMACÉN_11  12-01-2024) (2).xlsx'

# Cargar el archivo existente con openpyxl
book = load_workbook(archivo_dos_path)

# Crear un objeto ExcelWriter con el libro cargado
writer = pd.ExcelWriter(archivo_dos_path, engine='openpyxl') 
writer.book = book

# Leer el contenido actual
archivo_dos = pd.read_excel(writer, sheet_name="Hoja1", header=9)

eleccion = input('¿Desea agregar una columna? (si/no): ')

if eleccion.lower() == "si":
    posicion = int(input("Ingrese el índice de donde quiere insertar la columna: "))
    nombre_columna = input("Ingrese el nombre de la columna: ")
    archivo_dos.insert(loc=posicion, column=nombre_columna, value="vacio")
    print(archivo_dos.columns)
else:
    print(archivo_dos.columns)
    print('continue')

# Escribir de nuevo en el libro
archivo_dos.to_excel(writer, sheet_name="Hoja1", index=False)

# Guardar cambios
writer.save()
  
