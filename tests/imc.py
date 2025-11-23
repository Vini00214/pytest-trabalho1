def calcular_imc(peso, altura):
    if altura == 0:
        raise ValueError("A altura não pode ser zero.")
    imc = peso / (altura ** 2)
    return round(imc, 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso"
    elif 29.9 <= imc < 34.9:
        return "Obesidade grau I"
    elif 34.9 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"
