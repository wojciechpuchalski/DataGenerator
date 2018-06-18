# dokumentacja: http://www.algorytm.org/numery-identyfikacyjne/regon.html


import random

def regon():
    random_number = random.randint(10000000, 99999999)

    control_sum = [int(i) for i in str(random_number)]

    balance_list = [8, 9, 2, 3, 4, 5, 6, 7]
    result = [a * b for a, b in zip(control_sum, balance_list)]
    list(map(int, result))
    modulo = sum(result) % 11
    if modulo >= 10:
        modulo =0
    else:
        modulo = modulo

    regon_final = str(random_number) + str(modulo)

    return regon_final
