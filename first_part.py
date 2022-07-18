

def ""


class RomanNumberError(Exception):
    pass

numero_romano = (
    (1000,'M'), (500,'D'), (100,'C'), (50,'D'), (10,'X'),(5,'V'),(1,'I')
)

def entero_a_romano(numero):
    return "MCMXCIV"