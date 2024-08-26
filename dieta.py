class Dieta:
    def __init__(self, quantidade, tipo):
        self.quantidade = quantidade
        self.tipo = tipo

    def obterInfo(self):
        return f"Tipo de alimento: {self.tipo}, Quantidade: {self.quantidade}"
