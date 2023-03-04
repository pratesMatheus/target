print('='*50)
print('Sequência de Fibonacci')
print('='*50)

n = int(input('Digite para mim quantos termos você deseja mostrar? '))

termo1 = 0
termo2 = 1
print('-'*25)
print('{} -> {}'.format(termo1, termo2), end='')

count = 3
while count <= n:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    count += 1
print(' -> the end...')
