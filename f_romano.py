

n_romanos = { 
    "1" : 'I', "2": 'II', "3": 'III',
    "4": 'IL', "5": 'V', "6": 'VI',
    "7": 'VII', "8": 'VIII', "9": 'IX',

    "10": 'X', "20": 'XX', "30": 'XXX',
    "40": 'XL', "50": 'L', "60": 'LX',
    "70": 'LXX', "80": 'LXXX', "90": 'XC',

    "100": 'C', "200": 'CC', "300": 'CCC',
    "400": 'CD', "500": 'D', "600": 'DC',
    "700": 'DCC', "800": 'DCCC', "900": 'CM'
    }


def entero_a_romano(numero):
    digitos = transform_num_dic(numero)   
    dic_n_romano = transform_rom_dic(digitos)
    numero_romano = transform_rom_list(dic_n_romano)         
    return numero_romano

def transform_num_dic(numero):
#    numero = "{:0>4d}".format(numero)
    numero = "{:0>4s}".format(numero)
    digitos = list(numero)

    ix = 0
    longitud = len(digitos)
    for n in numero:
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        ix += 1
    return digitos
    
def transform_rom_dic(digitos):
    dic_n_romano = []
    for i in digitos:
        n_rom = n_romanos.get(i)
        dic_n_romano.append(n_rom)    
    return dic_n_romano

def transform_rom_list(dic_n_romano):
    numero_romano = ''
    for valor_romano in dic_n_romano:       
        if valor_romano != None:
            numero_romano += valor_romano         
    return numero_romano


valor = input("valor:")

valor_romano = entero_a_romano(valor)
print(valor_romano)




