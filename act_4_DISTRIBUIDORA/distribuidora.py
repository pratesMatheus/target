print('='*50)
print('Calculando o parcelamento mensal de uma distribuidora')
print('='*50)


def porcentagem(state, total):
    return round(((state*100)/total), 2)


sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros

print(f'Faturamento de SP em &: {str(porcentagem(sp, total))}%')
print('-'*25)
print(f'Faturamento de RJ em &: {str(porcentagem(rj, total))}%')
print('-'*25)
print(f'Faturamento de MG em &: {str(porcentagem(mg, total))}%')
print('-'*25)
print(f'Faturamento de ES em &: {str(porcentagem(es, total))}%')
print('-'*25)
print(
    f'Outros faturamentos em %: {str(porcentagem(outros, total))}%')

print('='*50)
