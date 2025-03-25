#Mini projeto para prática que visa a criação de um simples validador de CPF.

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    if int(cpf[9]) != digito1:
        return False

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    return int(cpf[10]) == digito2
# Exemplo de uso
cpf = input("Digite o CPF a ser validado: ")
print("CPF válido" if validar_cpf(cpf) else "CPF inválido")