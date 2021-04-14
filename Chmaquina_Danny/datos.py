
codigo_ch = []  #archivo.ch guardado en una lista
memoria = []  #lista memoria
errores = []  #lista de errores
variables = []
valores_variables = []
tipo_variables = []
etiquetas = []
valores_etiquetas = []

texto_monitor = []
texto_impresora = []

acumulador = [0]  #solo es un valor acumulador[0]

tam_kernel = [69]  #se actualiza cuando el usuario asigna el kernel
tam_memoria = [100]  #se actualiza cuando el usuario asigna la memoria

def datos_ker_mem(tam_ker, tam_mem):
    tam_kernel[0] =int(tam_ker)
    tam_memoria[0] =int(tam_mem)
    print("ASIGNAMOS y ahora tammemoria y tam_mem son", tam_memoria, " y " , tam_kernel)

