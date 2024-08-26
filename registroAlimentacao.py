class RegistroAlimentacao:
    def __init__(self, animal, dieta, data, quantidadeDada):
        self.animal = animal
        self.dieta = dieta
        self.data = data
        self.quantidadeDada = quantidadeDada
    def info(self):
        return f"Animal: {self.animal.nome}, Data: {self.data}, Quantidade Dada: {self.quantidadeDada}kg"
