from codigo.byte_bank import Funcionario

# gilmar = Funcionario('Gilmar','01/09/1983',1000)

# print(gilmar.idade())

def teste_idade():
    funcionario_teste = Funcionario('Gilmar', '01/09/1983',1114)
    print(f'Teste: {funcionario_teste.idade()}')

teste_idade()