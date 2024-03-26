# funcoes.py
from database import Dados

dados = Dados()

def cadastrar_veiculo(veiculo):
    dados.adicionar_veiculo(veiculo)

def cadastrar_motorista(motorista):
    dados.adicionar_motorista(motorista)

def listar_veiculos():
    return dados.obter_veiculos()

def listar_motoristas():
    return dados.obter_motoristas()

def relatorio_veiculos_por_motorista(motorista):
    veiculos_do_motorista = [veiculo for veiculo in dados.obter_veiculos() if veiculo["motorista"] == motorista]
    return veiculos_do_motorista

def relatorio_todos_veiculos():
    return dados.obter_veiculos()

def relatorio_todos_motoristas():
    return dados.obter_motoristas()

def apagar_veiculo(placa):
    dados.veiculos = [veiculo for veiculo in dados.veiculos if veiculo["placa"] != placa]

def atualizar_veiculo(placa, novo_veiculo):
    for veiculo in dados.veiculos:
        if veiculo["placa"] == placa:
            veiculo.update(novo_veiculo)
            break
