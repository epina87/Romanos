from turtle import position

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

simbolos_romanos  = {
    'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, '': 0
}

simbolos_romanos_resta  = {
    'I': ('V','X'), 'X':('L','C'), 'C': ('D','M'), '':('none')
}

class RomanNumberError(Exception):
    pass

def entero_a_romano(numero):
    numero = "{:0>4d}".format(numero)
    digitos = list(numero)

    longitud = len(digitos)
    romano = ''
    for ix in range(len(numero)):
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        romano += componentes.get(int(digitos[ix]), "")

    return romano

simbolos_romanos  = {
    'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, '': 0
}
 
simbolos_romanos_resta  = {
    'I': ('V','X'), 'X':('L','C'), 'C': ('D','M'), '':('none')
}

def romano_a_entero(romano: str) -> int:
    r = 0
    cont_repes = 1
    car_anterior = ""
    for pos,caracter in enumerate(romano):
        #Control repeticion 3 Max.
        if caracter == car_anterior:
            cont_repes += 1
        else:
            cont_repes = 1        
        if cont_repes > 3:
            raise RomanNumberError("No se pueden dar más de tres repeticiones")

        #Control calculo con mayor que el anterior
        if simbolos_romanos[caracter] > simbolos_romanos[car_anterior]:
            r -= simbolos_romanos[car_anterior] * 2

            #control "V", "L" y "D" nunca se pueden restar.
            tupla_resta = simbolos_romanos_resta.get(car_anterior,'error')
            if tupla_resta == 'error':
                raise RomanNumberError("Solo se puede restar 'I', 'X', 'C'")  
           
            elif tupla_resta != 'none':
                #control restas con valores correctos
                if tupla_resta[0] == caracter or tupla_resta[1] == caracter:
                    #Control restar digitos respectivos
                    posicion_2_anterior = pos - 1
                    if posicion_2_anterior!= 0 and car_anterior == romano[posicion_2_anterior]:
                        raise RomanNumberError("No se pueden restar repetidos")     
                else:
                    raise RomanNumberError("No se pueden restar")  
          
        r += simbolos_romanos[caracter]
        car_anterior = caracter
    
        #control  "D", "L" y "V" no se pueden repetir.
        if cont_repes >1 and str(simbolos_romanos[caracter])[0] == '5':
            raise RomanNumberError("No se puede repetir 'D','L','V'")    
            
    return r

    