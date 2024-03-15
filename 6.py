team1, team2 = map(int, input('Введите счет: ').split(':'))
if team1 > team2:
    print('Выигрывает команда номер 1')
elif team1 < team2:
    print('Выигрывает команда номер 2')
else:
    print(0)
