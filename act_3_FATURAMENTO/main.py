import json


def main():
    file = open('./act_3_FATURAMENTO/data/data.json')
    vetor = json.load(file)
    file.close()

    menor = min(map(lambda x: float(x['value']), vetor))
    print(f'- Menor valor de faturamento ocorrido em um dia do mês: {menor}')

    maior = max(map(lambda x: float(x['value']), vetor))
    print(f'- Maior valor de faturamento ocorrido em um dia do mês: {maior}')

    soma = sum(map(lambda x: float(x['value']), vetor))
    count = len(vetor)
    media = soma / count
    quantidade = sum(map(lambda x: 1 if int(x['value']) > media else 0, vetor))
    print(
        f'- N° de dias/M onde o faturamento p/dia superou a média mensal: {quantidade}')


if __name__ == "__main__":
    main()

"""
- Menor valor de faturamento ocorrido em um dia do mês: 0.0
- Maior valor de faturamento ocorrido em um dia do mês: 46251.1749
- N° de dias/M onde o faturamento p/dia superou a média mensal: 9
"""
