from animal import Animal
from dieta import Dieta
from registroAlimentacao import RegistroAlimentacao
from diarioAlimentacao import DiarioAlimentacao
from datetime import date

leao = Animal("Leão")
dietaLeao = Dieta("Carne", 10)
diario = DiarioAlimentacao()

diario.registroAlimentacao(leao, dietaLeao, 10)

diario.listar()

print(dietaLeao.obterInfo())