import calendar
ano = int(input('Digite um ano?'))
if calendar.isleap (ano):
    print('Este ano é BISSEXTO')
else:
    print('Este ano NÃO é BISSEXTO')
