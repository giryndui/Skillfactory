# Дан словарь per_cent с распределением процентных ставок по вкладам в различных
# банках таким образом, что ключ — название банка, значение — процент.
# Напишите программу, в результате которой будет сформирован список
# deposit значений — накопленные средства за год вклада в каждом из банков.
# На вход программы с клавиатуры вводится сумма money, которую человек планирует положить под проценты.
deposit = []
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28,'СБЕР': 4.0}
money=int(input('Введите сумму планируемую положить под проценты:'))
for i in per_cent:
    deposit.append(per_cent[i] * money / 100)
deposit=list(map(round, deposit))
print(deposit)
#Добавьте в программу поиск максимального значения и его вывод на экран:
print('Максимальная сумма, которую вы можете заработать-' + str(max(deposit)))






