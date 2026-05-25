import re

REGEX_IMPORTE = re.compile(r"^\d+([.,]\d{1,2})?$")
REGEX_FECHA   = re.compile(r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$")

class ErrorValidacion(Exception):
    pass

def test_importe_valido():
    assert REGEX_IMPORTE.match("12")
    assert REGEX_IMPORTE.match("12.50")
    assert REGEX_IMPORTE.match("12,50")
    print("test_importe_valido")

def test_importe_invalido():
    assert not REGEX_IMPORTE.match("abc")
    assert not REGEX_IMPORTE.match("12.999")
    assert not REGEX_IMPORTE.match("")
    print("test_importe_invalido")

def test_fecha_valida():
    assert REGEX_FECHA.match("19/02/1990")
    assert REGEX_FECHA.match("01/01/2024")
    print("test_fecha_valida")

def test_fecha_invalida():
    assert not REGEX_FECHA.match("32/01/2024")
    assert not REGEX_FECHA.match("19-02-1990")
    assert not REGEX_FECHA.match("hola")
    print("test_fecha_invalida")

def test_excepcion_validacion():
    try:
        raise ErrorValidacion("Importe no valido")
    except ErrorValidacion as e:
        assert str(e) == "Importe no valido"
    print("test_excepcion_validacion")

if __name__ == "__main__":
    test_importe_valido()
    test_importe_invalido()
    test_fecha_valida()
    test_fecha_invalida()
    test_excepcion_validacion()
    print("tos los tests pasan de maravii")