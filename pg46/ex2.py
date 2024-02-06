numero = 0.0
n = float(input(f"Digite um número: "))
while n >= numero:
    numero = n 
    n = float(input("Digite outro número: "))
    if n < numero:
        print("Obrigado")