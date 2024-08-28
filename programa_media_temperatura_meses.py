meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]

soma_temperaturas = sum(temperaturas)
qnt_meses = 12
media_nacional = soma_temperaturas / qnt_meses

print(f'{media_nacional:.1f}')
print()
print(f'Os meses que tiveram temperaturas acima da media são:')
print()
for i, temperatura in enumerate(temperaturas):
    if temperatura > media_nacional:
        print(temperaturas[i], meses[i])

print()
print(f'Os meses que tiveram temperaturas Abaixo da media são:')
print()
for i, temperatura in enumerate(temperaturas):
    if temperatura < media_nacional:
        print(temperaturas[i], meses[i])