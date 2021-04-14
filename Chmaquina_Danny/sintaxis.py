from datos import codigo_ch, errores, variables, valores_variables,tipo_variables, etiquetas, valores_etiquetas, memoria, tam_memoria

def verificar_sintaxis(codigo_ch):
    errores.clear()
    variables.clear()
    valores_variables.clear()
    tipo_variables.clear()
    etiquetas.clear()
    valores_etiquetas.clear()
    
    item = []
    lin_rev = 1
    for linea_cod in codigo_ch:
        #importate1 print("linea: ", lin_rev)
        #importante1 print(linea_cod, end = "" )
        linea_cod = linea_cod.strip("\n")
        item = linea_cod.split(" ")

        while("" in item): 
            item.remove("")

        #importante1 print(item)
        #importate1 print()
        if(item[0] == "cargue"): 
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "almacene"):  
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "nueva"):  
            error_funcion_nueva(item, lin_rev)
        elif(item[0] == "lea"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "sume"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "reste"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "multiplique"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "divida"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "potencia"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "modulo"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "concatene"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "elimine"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "extraiga"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "Y"):
            error_funcion_Y_O_NO(item, lin_rev)
        elif(item[0] == "O"):
            error_funcion_Y_O_NO(item, lin_rev)
        elif(item[0] == "NO"):
            error_funcion_Y_O_NO(item, lin_rev)
        elif(item[0] == "muestre"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "imprima"):
            error_funciones_1_operando(item, lin_rev)
        elif(item[0] == "vaya"):
            None
        elif(item[0] == "vayasi"):
            None
        elif(item[0] == "etiqueta"):
            error_funcion_etiqueta(item, lin_rev)
        elif(item[0] == "XXX"):
            None                                      #falta definir la función
        elif(item[0] == "retorne"):
            error_retorne(item, lin_rev)
        elif(item[0] == "" or item[0] == " "):
            errores.append("Linea " + str(lin_rev) + ":  " +"Error de identación")
        elif(es_comentario(item[0]) == True): 
            None # no hace nada porque un comentario no es un error de sintaxis
        else:
            errores.append("Linea " + str(lin_rev) + ":  " +"La función '" + item[0] + "' no ha sido definida")
        item.clear()
        lin_rev +=  1
    
    #print("LLEGAMOS A SINTAXIS CON ", tam_memoria)
    if(len(memoria)+len(codigo_ch) > tam_memoria[0]):
        errores.append("CRITICO: MEMORIA INSIFICIENTE")
        


def error_funciones_1_operando(item, lin_rev): 
    if(len(item)>2):
        errores.append("Linea " + str(lin_rev) + ":  " +"Excede el numero de operaciones/operandos")
    elif(nombre_var_valido(item[1]) == False):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[1]+ "' No es una variable valida: Error de nombre o nombre reservado")
    elif(item[1] not in variables):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[1]+ "' variable no ha sido declarada -> 'nueva nombre_var tipo valor'")

def error_funcion_nueva(item, lin_rev):
    tipos_de_datos = ["C","I", "R", "L"]
    if(len(item)>4):
        errores.append("Linea " + str(lin_rev) + ":  " +"Excede el numero de operaciones/operandos")
    elif(nombre_var_valido(item[1]) == False):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[1]+ "' nombre de variable NO válido")
    elif(item[2] not in tipos_de_datos):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[2]+ "' Tipo de dato inválido")
    elif(item[2] == "I" and not item[3].isdigit()):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[3]+ "' No pertenece al tipo de dato <"+ item[2] +">  especificado")
    elif(item[2] == "L" and not(item[3] == "1" or item[3] == "0")):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[3]+ "' No pertenece al tipo de dato <"+ item[2] +"> especificado")
    else:
        variables.append(item[1])
        valores_variables.append(item[3])
        tipo_variables.append(item[2])

def error_funcion_Y_O_NO(item, lin_rev): #Y var1 var2 respuesta
    if(len(item)>4): 
        errores.append("Linea " + str(lin_rev) + ":  " +"Excede el numero de operaciones/operandos")
    elif(item[1] not in variables):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[1]+ "' variable no ha sido declarada -> 'nueva nombre_var tipo valor'")
    elif(item[2] not in variables):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[2]+ "' variable no ha sido declarada -> 'nueva nombre_var tipo valor'")
    elif(item[3] not in variables):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[3]+ "' variable no ha sido declarada -> 'nueva nombre_var tipo valor'")

def error_funcion_etiqueta(item, lin_rev):
    if(len(item)>3):
        errores.append("Linea " + str(lin_rev) + ":  " +"Excede el numero de operaciones/operandos")
    elif(nombre_var_valido(item[1]) == False):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[1]+ "' No es una variable valida: Error de nombre o nombre reservado")
    elif(item[1] in variables):
        errores.append("Linea " + str(lin_rev) + ":  " + " '" + item[1]+ "' variable YA ha sido declarada")
    else:
        etiquetas.append(item[1])
        valores_etiquetas.append(item[2])

def error_retorne(item, lin_rev):
    if(len(item)>2): 
       errores.append("Linea " + str(lin_rev) + ":  " +"Excede el numero de operaciones/operandos") 


def nombre_var_valido(palabra):
    funciones_posibles = ["cargue", "almacene", "nueva", "lea", "sume", "reste", "multiplique", "divida", "potencia", 
        "modulo", "concatene", "elimine", "extraiga", "Y", "O", "NO", "muestre", "imprima", "vaya", "vayasi", "etiqueta", "XXX", "retorne"]
    if(palabra in funciones_posibles):
        return False
    else:
        cadena = ""
        cadena = palabra
        cadena = cadena[0: 1]
        #importante11 print("la cedena es: ", cadena)
        
        if(cadena.isdigit()):
            return False
    return True

def es_comentario(palabra): 
    cadena = ""
    cadena = palabra
    cadena = cadena[0: 2]
    #importante11 print("El comenntario es:< ", palabra, ">")
    return (cadena == "//")

def es_numero(palabra): 
    return (palabra.isdigit())

#función estetica para mostrar memoria------
def dir_estetica(numero):
    if(len(str(numero)) == 1):
        return "000"+ str(numero)
    elif(len(str(numero)) == 2): 
        return "00" + str(numero)
    elif(len(str(numero)) == 3): 
        return "0" + str(numero)
    else:
        return str(numero)


