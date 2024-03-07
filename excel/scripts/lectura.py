import pandas as pd

cols = ['NUMERO PLACA','DESCRIPCION','UBICACION'] #Esto se mandara como valor del argumento usecols

df = pd.read_excel(".\\excel\\input\\INVENTARIO 31DIC.xlsx", sheet_name= "Hoja2", header= 0, usecols=cols)

# io (str, buffer de bytes, ExcelFile, xlrd.Book, path or ExcelWriter):
# Especifica la ruta del archivo Excel o el objeto que contiene los datos.

# sheet_name (str, int, list, or None, default 0):
# Especifica qué hoja leer en el archivo Excel. Puede ser el nombre de la hoja (str), el índice de la hoja (int), una lista de nombres/índices o None (leer todas las hojas).

# header (int, list of int, default 0):
# Especifica qué fila debe usarse como encabezado. Puede ser un número entero (índice de fila) o una lista de números enteros para usar varias filas como encabezado.

# names (array-like, optional):
# Una lista de nombres que se utilizarán como nombres de columna. Si se proporciona, anulará cualquier encabezado que se encuentre en el archivo.

# index_col (int, str, sequence[int/str], or False, default None):
# Columna(s) para usar como índice de DataFrame. Si es None, no se utiliza ninguna columna como índice.

# usecols (int, str, sequence[int/str], or callable, optional):
# Columna(s) a leer del archivo. Puede ser el nombre de la columna, el índice o una secuencia de estos.

# skiprows (list-like, int or callable, optional):
# Filas a omitir durante la lectura del archivo.

# nrows (int, optional):
# Número de filas a leer desde la hoja.

# skipfooter (int, default 0):
# Número de filas al final del archivo que se deben omitir.

# converters (dict, default None):
# Un diccionario que especifica cómo convertir los datos en ciertas columnas. La clave es el nombre de la columna o el índice, y el valor es una función o tipo de datos que realiza la conversión.

nuevo = df[df["NUMERO PLACA"] == 101581]

print(nuevo)

hola = input("ingrese")