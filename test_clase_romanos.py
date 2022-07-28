from tkinter import N
from romanos_class import NumeroRomano

def test_crear_instancia_numero_romano():
    nr = NumeroRomano(34)
    otronr = NumeroRomano(30)
    assert str(nr) == 'XXXIV'
    assert str(otronr) == 'XXX'


def test_crear_instancia_numero_romano_desde_cadena():
    nr = NumeroRomano('XXXI')
    assert str(nr) == 'XXXI'
    assert nr.valor == 31


def test_suma_romanos():
    nr1 = NumeroRomano('XX')
    nr2 = NumeroRomano(30)

    nr3 = nr1 + nr2

    assert isinstance(nr3, NumeroRomano) == True
    assert nr3.valor == 50
    assert nr3.representacion == "L"

def test_suma_romanos_entero():
    nr1 = NumeroRomano('XX')
    nr2 = NumeroRomano(30)

    nr3 = nr1 + 30
    nr4 = 30 + nr1 

    assert isinstance(nr3, NumeroRomano) == True
    assert nr3.valor == 50
    assert nr3.representacion == "L"

    assert isinstance(nr4, NumeroRomano) == True
    assert nr4.valor == 50
    assert nr4.representacion == "L"

def test_restar_romanos():
    nr1 = NumeroRomano('XX')
    nr2 = NumeroRomano(30)

    nr3 = nr2 - nr1
    nr4 = 30 - nr1 

    assert isinstance(nr3, NumeroRomano) == True
    assert nr3.valor == 10
    assert nr3.representacion == "X"

    assert isinstance(nr4, NumeroRomano) == True
    assert nr4.valor == 10
    assert nr4.representacion == "X"


def test_multiplicar_romanos():
    nr1 = NumeroRomano('V')
    nr2 = NumeroRomano(2)

    nr3 = nr1 * nr2
    nr4 = 2 * nr1 

    assert isinstance(nr3, NumeroRomano) == True
    assert nr3.valor == 10
    assert nr3.representacion == "X"

    assert isinstance(nr4, NumeroRomano) == True
    assert nr4.valor == 10
    assert nr4.representacion == "X"

def test_dividir_romanos():
    nr1 = NumeroRomano('X')
    nr2 = NumeroRomano(2)

    nr3 = nr1 // nr2
    nr4 = 10 // nr2 

    assert isinstance(nr3, NumeroRomano) == True
    assert nr3.valor == 5
    assert nr3.representacion == "V"

    assert isinstance(nr4, NumeroRomano) == True
    assert nr4.valor == 5
    assert nr4.representacion == "V"




