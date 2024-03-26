# main.py
from lib import funcoes

def menu():
    print("1. Cadastrar veículo")
    print("2. Cadastrar motorista")
    print("3. Listar veículos")
    print("4. Listar motoristas")
    print("5. Relatório de veículos por motorista")
    print("6. Relatório de todos os veículos")
    print("7. Relatório de todos os motoristas")
    print("8. Apagar veículo")
    print("9. Atualizar veículo")
    print("0. Sair")

def cadastrar_veiculo():
    placa = input("Digite a placa do veículo: ")
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    motorista = input("Digite o motorista do veículo: ")
    veiculo = {"placa": placa, "marca": marca, "modelo": modelo, "motorista": motorista}
    funcoes.cadastrar_veiculo(veiculo)
    print("Veículo cadastrado com sucesso!")

def cadastrar_motorista():
    nome = input("Digite o nome do motorista: ")
    idade = input("Digite a idade do motorista: ")
    cnh = input("Digite a CNH do motorista: ")
    motorista = {"nome": nome, "idade": idade, "cnh": cnh}
    funcoes.cadastrar_motorista(motorista)
    print("Motorista cadastrado com sucesso!")

def listar_veiculos():
    veiculos = funcoes.listar_veiculos()
    for veiculo in veiculos:
        print(veiculo)

def listar_motoristas():
    motoristas = funcoes.listar_motoristas()
    for motorista in motoristas:
        print(motorista)

def relatorio_veiculos_por_motorista():
    motorista = input("Digite o nome do motorista: ")
    veiculos = funcoes.relatorio_veiculos_por_motorista(motorista)
    for veiculo in veiculos:
        print(veiculo)

def relatorio_todos_veiculos():
    veiculos = funcoes.relatorio_todos_veiculos()
    for veiculo in veiculos:
        print(veiculo)

def relatorio_todos_motoristas():
    motoristas = funcoes.relatorio_todos_motoristas()
    for motorista in motoristas:
        print(motorista)

def apagar_veiculo():
    placa = input("Digite a placa do veículo a ser apagado: ")
    funcoes.apagar_veiculo(placa)
    print("Veículo apagado com sucesso!")

def atualizar_veiculo():
    placa = input("Digite a placa do veículo a ser atualizado: ")
    marca = input("Digite a nova marca do veículo: ")
    modelo = input("Digite o novo modelo do veículo: ")
    motorista = input("Digite o novo motorista do veículo: ")
    novo_veiculo = {"marca": marca, "modelo": modelo, "motorista": motorista}
    funcoes.atualizar_veiculo(placa, novo_veiculo)
    print("Veículo atualizado com sucesso!")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_veiculo()
        elif opcao == "2":
            cadastrar_motorista()
        elif opcao == "3":
            listar_veiculos()
        elif opcao == "4":
            listar_motoristas()
        elif opcao == "5":
            relatorio_veiculos_por_motorista()
        elif opcao == "6":
            relatorio_todos_veiculos()
        elif opcao == "7":
            relatorio_todos_motoristas()
        elif opcao == "8":
            apagar_veiculo()
        elif opcao == "9":
            atualizar_veiculo()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
