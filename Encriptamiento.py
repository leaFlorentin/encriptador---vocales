# ---- ENCRIPATADO/ DESECRIPTADO DE PALABRAS ---

CODIGO_LLAVE = {
    "a" : "ai",
    "e" : "enter",
    "i" : "imes",
    "o" : "ober",
    "u" : "ufat"
}


def desencriptar_palabra(texto, indice):

    palabra_cod_llave = CODIGO_LLAVE.get(texto[indice])

    if texto.startswith(palabra_cod_llave , indice) == True:
        return texto[indice], len(palabra_cod_llave )
    else:
        return texto[indice], 1


def desencriptar(texto):

    texto_desencriptado = []
    i = 0

    while i < len(texto): # len(texto) = 8

        if texto[i] in CODIGO_LLAVE:
            text, cant_saltos = desencriptar_palabra(texto, i)
            texto_desencriptado.append(text)
            i+= cant_saltos
        else:
            texto_desencriptado.append(texto[i])
            i+=1
    
    nuevo_texto = "".join(texto_desencriptado)
    return nuevo_texto


def encriptar(txt):
    #Captura el texto para luego encriptarlo
    texto_encriptado = []

    for t in txt:
        if t in CODIGO_LLAVE: 
            texto_encriptado.append(CODIGO_LLAVE.get(t))
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
    texto = input("Dime el texto a desencriptar").lower()
    print(desencriptar(texto))
    


while True:

    try:
        opcion = int(input("Elige la opcion: 1- Encriptar | 2- Desencriptar | 3- Salir"))

        if opcion == 3:
            print("Saliendo de la app....")
            break
        
        if opcion == 1:
            encriptar_txt()
        elif opcion == 2:
            desencriptar_txt()
            
    except ValueError:
        print("Error de opcion, vuelva a intentar")
