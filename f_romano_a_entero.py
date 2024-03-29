
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
    error = ""
    dic_romano = conbertir_dic_romano() 

    n_romano2 = n_romano
    numero_entero = 0
    posicion_n_romano = 0
    while posicion_n_romano<len(n_romano):   

        n =  n_romano[posicion_n_romano]
        valor_entero = dic_romano.get(n,"error") 
        if valor_entero == "error":
            numero_entero = 0
            error = "Valores Incorrectos"
            break 
        
        ix=posicion_n_romano + 1

        contador_posiciones_sumar = 0
        contador_valores_iguales  = 1

        valor_entero_final = 0
        while ix<len(n_romano2):            
            valor_siguiente = n_romano[ix]
            valor_entero_siguiente = dic_romano.get(valor_siguiente,"error") 
            if valor_entero_siguiente == "error":
                error = "Valores Incorrectos"
                break
            elif valor_entero_siguiente > valor_entero:
                posicion_anterior = ix - 1
                if posicion_anterior != 0:
                    valor_anterior = n_romano[posicion_anterior]
                    valor_entero_anterior =  dic_romano.get(valor_anterior,"")
                else:
                    valor_entero_anterior = 0    
                    
                valor_entero_restado,error = restar_valor(valor_entero,valor_entero_siguiente,valor_entero_anterior)
                if error == "":
                    valor_entero_final += valor_entero_restado
                else:
                    break
                contador_posiciones_sumar += 1 
            elif valor_entero_siguiente == valor_entero:
                contador_valores_iguales += 1
            else:   
                break           
            ix += 1 

        if contador_valores_iguales > 3 or error!="":
            numero_entero = 0
            error = "El número romano no es correcto"
            break
        if valor_entero_final != 0:
            valor_entero = valor_entero_final       

        numero_entero += valor_entero     
        posicion_n_romano += 1 + contador_posiciones_sumar
    
    return numero_entero,error

def restar_valor(valor_entero,valor_entero_siguiente,valor_entero_anterior):
    error = ''
    if valor_entero_anterior == valor_entero:
        valor_entero_restado = 0
        error = "El número romano no es correcto"
    else:        
        if valor_entero== 1 and (valor_entero_siguiente ==5 or valor_entero_siguiente ==10 ):
            valor_entero_restado = valor_entero_siguiente - valor_entero
        elif valor_entero== 10 and (valor_entero_siguiente ==50 or valor_entero_siguiente ==100 ):
            valor_entero_restado = valor_entero_siguiente - valor_entero
        elif valor_entero== 100 and (valor_entero_siguiente ==500 or valor_entero_siguiente ==1000 ):
            valor_entero_restado = valor_entero_siguiente - valor_entero
        else:
            valor_entero_restado = 0
            error = "El número romano no es correcto"

    return valor_entero_restado,error


valor = input("Número romano:").upper()
valor_romano,error = romano_a_entero(valor)
if error == "":
    print("Valor entero: ",  valor_romano)
else:
    print(error)
     
     