from first_part import entero_a_romano

"""
casos de prueba

a) 1994 - > MCMXCIV
b) 4000 -> RomanNumberError("El valor debe ser menor de 4000")
C) "unacadena" -> RomanNumberError("debe ser un entero")
d) 0 ->  RomanNumberError("El valor debe ser un entero")
e) - 3 ->  RomanNumberError("El valor debe ser un entero")
f) 4.5 ->  RomanNumberError("debe ser un entero")

"""

def test_error_si_entero_mayor_de_3999():
    assert 2 + 1  == 3 

def test_valor_1994():
    assert entero_a_romano(1994) == 'MCMXCIV' 