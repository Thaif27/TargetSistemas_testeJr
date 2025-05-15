import json

with open('dados.json', 'r') as f:# ler o arquivo json
    dados = json.load(f)


faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0] #faz a filtragem dos dias de faturamento maior que 0


menor = min(faturamentos)
maior = max(faturamentos)
media = sum(faturamentos) / len(faturamentos)
dias_acima_da_media = sum(1 for valor in faturamentos if valor > media)


print(f"Menor faturamento: R$ {menor:.2f}")
print(f"Maior faturamento: R$ {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
