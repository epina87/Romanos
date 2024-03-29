from cmath import e


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

restas  = {
    'I': ('V', 'X'), 
    'X': ('L', 'C'), 
    'C': ('D', 'M'), 
}

numeros_romanos = 'IVXLCDM'

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

def romano_a_entero(romano: str) -> int:
    r = 0
    cont_repes = 1
    car_anterior = ""
    for caracter in romano:
        if caracter == car_anterior:
            cont_repes += 1
        else:
            cont_repes = 1 

        if cont_repes > 3:
            raise RomanNumberError("No se pueden dar más de tres repeticiones")
        
        if simbolos_romanos[caracter] > simbolos_romanos[car_anterior]:
        # Forma de diccionario restas
            if car_anterior not in restas.keys():
                raise RomanNumberError("El simbolo {} no puede restar".format(car_anterior))

            if caracter in restas[car_anterior]:
                pass
            else:
                raise RomanNumberError(f"{car_anterior} solo se puede restar a {restas[car_anterior][0]} y {restas[car_anterior][1]}")         

        # Forma de ifs a capon
            if car_anterior == 'I' and caracter != 'X' and caracter != 'V':
                raise RomanNumberError("I solo se puede restar a V y X")
            if car_anterior == 'X' and caracter != 'L' and caracter != 'C':
                raise RomanNumberError("X solo se puede restar a L y C")
            if car_anterior == 'C' and caracter != 'D' and caracter != 'M':
                raise RomanNumberError("I solo se puede restar a V y X")

        # Forma de Alfredo
            if car_anterior not in "IXC" or numeros_romanos.index(caracter) - numeros_romanos.index(car_anterior) > 2:
                raise RomanNumberError(f"{car_anterior} solo se puede restar a {numeros_romanos[numeros_romanos.index(car_anterior) + 1]} y {numeros_romanos[numeros_romanos.index(car_anterior) + 2]}")

            

            r -= simbolos_romanos[car_anterior] * 2


        r += simbolos_romanos[caracter]
        car_anterior = caracter
    

    return r