
n_romanos = { 
    "1" : 'I', "2": 'II', "3": 'III',
    "4": 'IL', "5": 'V', "6": 'VI',
    "7": 'VII', "8": 'VIII', "9": 'IX',

    "10": 'X', "20": 'XX', "30": 'XXX',
    "40": 'XL', "50": 'L', "60": 'LX',
    "70": 'LXX', "80": 'LXXX', "90": 'XC',

    "100": 'C', "200": 'CC', "300": 'CCC',
    "400": 'CD', "500": 'D', "600": 'DC',
    "700": 'DCC', "800": 'DCCC', "900": 'CM',

    "1000":'M', "2000":'MM',"3000":'MMM'
    }


def entero_a_romano(numero):
    numero_romano = ''
    
    numero = "{:0>4s}".format(numero)    
    longitud = len(numero)
    
    for n in numero:
        longitud -= 1
        digito = n + "0" * longitud

        valor_romano = n_romanos.get(digito)   
        if valor_romano != None:
            numero_romano += valor_romano      
              
    return numero_romano

valor = input("Número entero:")
valor_romano = entero_a_romano(valor)
print("Valor en romano: " +  valor_romano)