import pytest

from romanos_funcional2 import entero_a_romano, romano_a_entero, RomanNumberError

"""
Casos de prueba 
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("El valor debe ser menor de 4000")
c) "unacadena" -> RomanNumberError("Debe ser un entero")
d) 0 -> RomanNumberError("El valor debe ser mayor de cero")
e) -3 -> RomanNumberError("El valor debe ser mayor de cero")
f) 4.5 -> RomanNumberError("Debe ser un entero")


"""

def test_1336():
    assert entero_a_romano(1336) == 'MCCCXXXVI'

def test_336(): 
    assert entero_a_romano(336) == 'CCCXXXVI'

def test_romano_a_entero_ordenados():
    assert romano_a_entero('I') == 1
    assert romano_a_entero('MDCCXIII') == 1713

def test_romano_a_entero_no_mas_de_tres():

    with pytest.raises(RomanNumberError) as  exceptionInfo:
        romano_a_entero('LIIII')
    
    assert str(exceptionInfo.value) == "No se pueden dar más de tres repeticiones"


def test_romano_a_entero_resta_si_soy_mayor_que_anterior():
    assert romano_a_entero('IV') == 4


def test_romano_a_entero_no_repite_D_L_V():

    with pytest.raises(RomanNumberError) as  exceptionInfo:
        romano_a_entero('DD')
    
    assert str(exceptionInfo.value) == "No se puede repetir 'D','L','V'"


def test_romano_a_entero_restar_no_validos():

    with pytest.raises(RomanNumberError) as  exceptionInfo:
        romano_a_entero('VL')
    
    assert str(exceptionInfo.value) == "Solo se puede restar 'I', 'X', 'C'"

def test_romano_a_entero_restar_I():

    with pytest.raises(RomanNumberError) as  exceptionInfo:
        romano_a_entero('IL')
    
    assert str(exceptionInfo.value) == "No se pueden restar"


def test_romano_a_entero_restar_X():

    with pytest.raises(RomanNumberError) as  exceptionInfo:
        romano_a_entero('XM')
    
    assert str(exceptionInfo.value) == "No se pueden restar"

def test_romano_a_entero_restar_repetido():

    with pytest.raises(RomanNumberError) as  exceptionInfo:
        romano_a_entero('IIIX')
    
    assert str(exceptionInfo.value) == "No se pueden restar repetidos"


