class Dados:
    def __init__(self):
        self.veiculos = []
        self.motoristas = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def adicionar_motorista(self, motorista):
        self.motoristas.append(motorista)

    def obter_veiculos(self):
        return self.veiculos

    def obter_motoristas(self):
        return self.motoristas