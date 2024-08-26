from datetime import date
from registroAlimentacao import RegistroAlimentacao
class DiarioAlimentacao:
    def __init__(self):
        self.registro = []

    def registroAlimentacao(self, animal, dieta, quantidadeDada):
        novo_registro = RegistroAlimentacao(
            animal=animal,
            dieta=dieta,
            data=date.today(),
            quantidadeDada = quantidadeDada
        )
        self.registro.append(novo_registro)
    def listar(self):
        for registro in self.registro:
            print(registro)
