nome1 = input("Digite o nome do aluno 1:")
media1 = float(input(f"Digite a media do aluno {nome1}: "))
while media1 < 0 or media1 > 10:
    media1 = float(input("Digite o valor de 0-10 para média: "))

nome2 = input("Digite o nome do aluno 2:")
media2 = float(input(f"Digite a media do aluno {nome2}: "))
while media2 < 0 or media2 > 10:
    media2 = float(input("Digite o valor de 0-10 para média 2: "))

nome3 = input("Digite o nome do aluno 3:")
media3 = float(input(f"Digite a media do aluno {nome3}: "))
while media3 < 0 or media3 > 10:
    media3 = float(input("Digite o valor de 0-10 para média 3: "))

if media1 > media2 and media1 > media3:
    maior = media1
    aluno = nome1
    print(f"O {aluno} teve a maior média {maior}!")

if media2 > media1 and media2 > media3:
    maior = media2
    aluno = nome2
    print(f"O {aluno} teve a maior média {maior}!")

if media3 > media1 and media3 > media2:
    maior = media3
    aluno = nome3
    print(f"O {aluno} teve a maior média {maior}!")