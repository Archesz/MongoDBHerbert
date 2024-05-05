import re

def validar_name(name):
    if len(name) < 2 or len(name) > 400:
        return False
    else:
        return name.title()
    
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 11 - resto if resto >= 2 else 0

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 11 - resto if resto >= 2 else 0

    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True
    else:
        return False
    
def validar_celular(numero):
    padrao = re.compile(r'^\d{11}$')

    if padrao.match(numero):
        return True
    else:
        return False
    
def validar_email(email):
    padrao = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    if padrao.match(email):
        return True
    else:
        return False
    
def validar_cep(cep):
    padrao = re.compile(r'^\d{8}$')

    if padrao.match(cep):
        return True
    else:
        return False