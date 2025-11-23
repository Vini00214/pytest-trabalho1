import pytest
from imc import calcular_imc, classificar_imc

def test_calculo_imc_valor_correto():
    assert calcular_imc(70, 1.75) == 22.86

def test_arredondamento_imc():
    assert calcular_imc(80, 1.80) == 24.69

def test_altura_zero_erro():
    with pytest.raises(ValueError):
        calcular_imc(70, 0)

def test_classificacao_abaixo_peso():
    assert classificar_imc(17.9) == "Abaixo do peso"

def test_classificacao_normal():
    assert classificar_imc(22.0) == "Peso normal"

def test_classificacao_sobrepeso():
    assert classificar_imc(27.3) == "Sobrepeso"

def test_classificacao_obesidade_g1():
    assert classificar_imc(33.0) == "Obesidade grau I"

def test_classificacao_obesidade_g2():
    assert classificar_imc(37.0) == "Obesidade grau II"

def test_classificacao_obesidade_g3():
    assert classificar_imc(45.0) == "Obesidade grau III"
