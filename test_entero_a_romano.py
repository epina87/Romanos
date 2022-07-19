from first_part import entero_a_romano

"""
Casos de prueba 
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("El valor debe ser menor de 4000")
c) "unacadena" -> RomanNumberError("Debe ser un entero")
d) 0 -> RomanNumberError("El valor debe ser mayor de cero")
e) -3 -> RomanNumberError("El valor debe ser mayor de cero")
f) 4.5 -> RomanNumberError("Debe ser un entero")


"""

def test_descomposicion_336():
    assert entero_a_romano(336) == ['0000', '300', '30', '6'] #=> 'CCCXXXVI'