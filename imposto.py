s = float(input("Digite seu salário: "))
if s >= 2112.01 and s <= 2826.65:
    print(f"Seu imposto será de {s*75/1000} reais")
elif s >= 2826.66 and s <= 3751.05:
    print(f"Seu imposto será de {s*15/100} reais")
elif s >= 3751.06 and s <= 4664.68:
    print(f"Seu imposto será de {s*225/1000} reais")
elif s > 4664.68:
    print(f"Seu imposto será de {s*275/1000} reais")
else:
    print("Você não paga imposto de renda! :D")
    