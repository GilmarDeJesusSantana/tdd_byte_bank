from codigo.byte_bank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_200_deve_retornar_22(self):
        entrada = '13/03/2000'  # Given --> Contexto
        esperado = 22

        funcionario_teste = Funcionario('Gilmar', entrada, 1110)
        resultado = funcionario_teste.idade()  # When --> ação

        assert esperado == resultado  # Then --> desfecho

    def test_retorna_sobrenome_do_Gilmar_Santana(self):
        entrada = ' Gilmar Santana '
        esperado = 'Santana'

        funcionario_teste_sobrenome = Funcionario(entrada, '01/09/1983', 45111)
        resultado = funcionario_teste_sobrenome.sobrenome()
        assert resultado == esperado

    def test_quando_for_diretor_fazer_decrescimo_de_10_porcento_em_salario_de_100000(self):
        entrada_salario = 100000
        esperado = 90000

        entrada_nome = 'Paulo Bragança'

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    def test_calcular_bonus_quando_salario_1000_recebe_100(self):
        entrada = 1000 #Given
        esperado = 100

        funcionario = Funcionario('Gilmar', '01/05/1987', entrada)
        resultado = funcionario.calcular_bonus() #When

        assert resultado == esperado #Then


