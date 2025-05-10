faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}


total = sum(faturamento.values()) #faz o calculo total
#usamos "sum" sempre que formos calcular o valor total

for estado, valor in faturamento.items(): #calcular e exibir cada estado
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}% do total")
