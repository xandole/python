nome = (input("Digite o seu nome: "))
prova1 = float(input("Digite a nota da primeira prova: "))
while prova1 < 0 or prova1 > 10:
    prova1 = float(input("Digite o valor de 0-10 para prova 1: "))

prova2 = float(input("Digite a nota da segunda prova: "))
while prova2 < 0 or prova1 > 10:
    prova2 = float(input("Digite o valor de 0-10 para prova 2: "))

trabalho = float(input("Digite a sua nota de trabalho: "))
while trabalho < 0 or prova1 > 10:
    trabalho = float(input("Digite o valor de 0-10 para nora de trabalho: "))

media = prova1*0.35 + prova2*0.35 + trabalho*0.3
if media >= 5.0:
    situacao = "Aprovado"
elif media > 3.5 and media < 5.0:
    situacao = ("Recuperação")
else:
    situacao = ("Reprovado")

print(f"Olá, {nome}! sua média final foi {media}. Situação: {situacao}.")
