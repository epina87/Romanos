
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
  
def conbertir_dic_romano():
    dic_romano = {}
    for clave,valor in componentes.items():
        dic_romano[valor] = clave
    return dic_romano

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
            elif valor_entero_siguiente == valor_entero:
                contador_valores_iguales += 1
            else:   
                break
            
            ix += 1 

        if contador_valores_iguales > 3:
            numero_entero = 0
            print("El número romano no es correcto")
            break

        numero_entero += valor_entero        
        posicion_n_romano += 1 + contador_posiciones_sumar
    
    return numero_entero

valor = input("Número romano:")
valor_romano = romano_a_entero(valor)
print("Valor entero: ",  valor_romano)
        