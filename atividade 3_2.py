import xml.etree.ElementTree as ET #ElementTree é usado para ler e manipular arquivos XML.

tree = ET.parse('dados.xml') # carregar e analisar o arquivo
root = tree.getroot()

faturamentos = []

for row in root.findall('row'):
    valor_tag = row.find('valor')
    if valor_tag is not None:
        valor = float(valor_tag.text)
        if valor > 0:  # dias sem faturamento.
            faturamentos.append(valor)

if faturamentos:
    menor = min(faturamentos)
    maior = max(faturamentos)
    media = sum(faturamentos) / len(faturamentos)
    dias_acima_da_media = sum(1 for valor in faturamentos if valor > media)

    print(f"Menor faturamento: R$ {menor:.2f}")
    print(f"Maior faturamento: R$ {maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
else:
    print("Nenhum faturamento válido encontrado.")
