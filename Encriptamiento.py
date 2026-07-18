# ---- ENCRIPATADO/ DESECRIPTADO DE PALABRAS ---
VOCALES = ["a", "e", "i", "o", "u"]

CODIGO_LLAVE = {
    "a" : "ai",
    "e" : "enter",
    "i" : "imes",
    "o" : "ober",
    "u" : "ufat"
}

def encriptar_letra(letra):
    #Evalua cada caso de la letra capturada
    match letra:
        case "a":
            return "ai"
        case "e":
            return "enter"
        case "i":
            return "imes"
        case "o":
            return "ober"
        case "u":
            return "ufat"        
        case _:
            return letra



def desencriptar_palabra(texto, indice):
    if texto.startswith(CODIGO_LLAVE.get(texto[indice]), indice) == True:
        return texto[indice]
    else:
        return texto[indice]


def saltos_desencriptados(texto, indice):
    if texto.startswith(CODIGO_LLAVE.get(texto[indice]), indice) == True:
        return len(CODIGO_LLAVE.get(texto[indice]))
    else:
        return 1


def desencriptar(texto):

    texto_desencriptado = []
    i = 0

    while i < len(texto): # len(texto) = 8

        if texto[i] in CODIGO_LLAVE:
            texto_desencriptado.append(desencriptar_palabra(texto, i))
            i+= saltos_desencriptados(texto, i)
        else:
            texto_desencriptado.append(texto[i])
            i+=1
    
    nuevo_texto = "".join(texto_desencriptado)
    return nuevo_texto


def encriptar(txt):
    #Captura el texto para luego encriptarlo
    texto_encriptado = []

    for t in txt:
        if t in VOCALES: 
            letra_encriptada = encriptar_letra(t)
            texto_encriptado.append(letra_encriptada)
        else:
            texto_encriptado.append(t)

    #El join une los elementos del arreglo en un solo texto
    nuevo_texto = "".join(texto_encriptado)
    return nuevo_texto


def encriptar_txt():
    #Esta funcion encripta el texto que el usuario coloca
    texto = input("Dime el texto a encriptar").lower()
    print(encriptar(texto))

def desencriptar_txt():
    #Esta funcion desencripta el texto que el usuario coloca
    texto = input("Dime el texto a encriptar").lower()
    print(desencriptar(texto))
    


while True:
    opcion = int(input("Elige la opcion: 1- Encriptar | 2- Desencriptar | 3- Salir"))

    if opcion == 3:
        print("Saliendo de la app....")
        break

    try:
        if opcion == 1:
            encriptar_txt()
        elif opcion == 2:
            desencriptar_txt()
    except ValueError:
        print("Error de opcion, vuelva a intentar")
        continue

