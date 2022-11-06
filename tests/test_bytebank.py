import pytest
from pytest import mark

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

    @mark.calcular_bonus
    def test_calcular_bonus_quando_salario_1000_recebe_100(self):
        entrada = 1000  # Given
        esperado = 100

        funcionario = Funcionario('Gilmar', '01/05/1987', entrada)
        resultado = funcionario.calcular_bonus()  # When

        assert resultado == esperado  # Then

    @mark.calcular_bonus
    def test_quando_recebe_100000_deve_retorna_exeception(self):
        with pytest.raises(Exception):
            entrada = 100000  # Given

            funcionario = Funcionario('Fuc_Excep', '01/03/1998', entrada)
            resultado = funcionario.calcular_bonus()  # When

            assert resultado  # Then

    def test_certifica_retorno_str(self):
        nome, datanascimento, salario = 'Teste', '01/09/1983', 1000
        esperado = 'Funcionario: (Teste, 01/09/1983 ,1000)'

        funcionario = Funcionario(nome,datanascimento,salario)
        resultado = funcionario.__str__()

        assert  resultado == esperado
