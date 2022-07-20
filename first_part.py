"""
1. Crear una función que pase de entero > 0 y < 4000 a romano
2. Cualquier otra entrada debe dar error


"""

class RomanNumberError(Exception):
    pass

numero_romano = {
    1000: 'M', 500: 'D', 100: 'C', 50: 'D', 10: 'X', 5: 'V', 1: 'I'
}

algoritmo_romano = (
    {1: 'M'},
    {1: 'C', 5: 'D', 10: 'M'},
    {1: 'X', 5: 'L', 10: 'C'},
    {1: 'I', 5: 'V', 10: 'X'},
)


componentes = {
    1000: 'M', 2000: 'MM', 3000: 'MMM', 
    100: 'C', 200: 'CC', 300: 'CCC',
    400: 'CD', 500: 'D', 600: 'DC',
    700: 'DCC', 800: 'DCCC', 900: 'CM',
    10: 'X', 20: 'XX', 30: 'XXX',
    40: 'XL', 50: 'L', 60: 'LX',
    70: 'LXX', 80: 'LXXX', 90: 'XC',
    1: 'I', 2: 'II', 3: 'III',
    4: 'IL', 5: 'V', 6: 'VI',
    7: 'VII', 8: 'VIII', 9: 'IX'
}    


def entero_a_romano_2(numero):
    numero = "{:0>4d}".format(numero)
    digitos = list(numero)

    romano = ''

    for tipo_unidad, digito in enumerate(digitos):
        digito = int(digito)
        tupla_activa = algoritmo_romano[tipo_unidad]

        if digito < 4:
            romano += tupla_activa[1] * digito
        elif digito == 4:
            romano += tupla_activa[1] + tupla_activa[5]
        elif int(digitos[1]) < 9:
            romano += tupla_activa[5] + tupla_activa[1] * (digito - 5)
        else:
            romano += tupla_activa[1] + tupla_activa[10]

    return romano


def entero_a_romano(numero):
    """
    numero = str(numero)
    longitud = len(numero)

    if longitud < 4:
        numero = "{:0>4s}".format(numero)
    """
    numero = "{:0>4d}".format(numero)
    digitos = list(numero)

    longitud = len(digitos)
    romano = ''
    for ix in range(len(numero)):
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        romano += componentes.get(int(digitos[ix]), "")

    return romano


#------------------------------------------------Entero Romano    

def romano_a_entero(n_romano):
    dic_romano = conbertir_dic_romano() 

    n_romano2 = n_romano
    numero_entero = 0
    posicion_n_romano = 0
    while posicion_n_romano<len(n_romano):   

        n =  n_romano[posicion_n_romano]
        valor_entero = dic_romano.get(n,"")  
        ix=posicion_n_romano + 1
        contador_posiciones_sumar = 0
        contador_valores_iguales  = 0
        while ix<len(n_romano2):
            valor_siguiente = n_romano[ix]
            valor_entero_siguiente = dic_romano.get(valor_siguiente,"") 
            if valor_entero_siguiente > valor_entero:
                valor_entero = valor_entero_siguiente - valor_entero
                contador_posiciones_sumar += 1 
            if valor_entero_siguiente == valor_entero:
                contador_valores_iguales += 1

            ix += 1 

        if contador_valores_iguales > 3:
            numero_entero = 0
            print("El número romano no es correcto")
            break

        numero_entero += valor_entero        
        posicion_n_romano += 1 + contador_posiciones_sumar
    
    print(numero_entero)           

def conbertir_dic_romano():
    dic_romano = {}
    for clave,valor in componentes.items():
        dic_romano[valor] = clave
    return dic_romano
        


#1996 - MCMXCVI
#336  - CCCXXXVI
romano_a_entero("MCMXCVI")