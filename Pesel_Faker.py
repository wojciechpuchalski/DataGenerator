# Zgodnie z dokumentacja https://obywatel.gov.pl/dosuma_kontrolnaumenty-i-dane-osobowe/czym-jest-numer-pesel

import random


def pesel():

    year = random.randint(1, 99)
    if year <= 9:
        year = '0' + str(year)

    month = random.randint(1, 12)
    if month <= 9:
        month = '0' + str(month)

    day = random.randint(1, 29)
    if day <= 9:
        day = '0' + str(day)

    pppp = random.randint(1111, 9999)

    random_integers = str(year) + str(month) + str(day) + str(pppp)

    # sprawdzanie sumy kontrolnej
    control_sum = [int(i) for i in str(random_integers)]

    # sprawdzanie wagi dla sumy kontrolnej
    balance_list = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    result = [a * b for a, b in zip(control_sum, balance_list)]

    # jesli wynik > 9 to ucinam wynik tylko do miejsca jednostek
    for n, i in enumerate(result):
        if i > 9:
            i = str(i)
            result[n] = i[1]
    results = list(map(int, result))
    k = sum(results)
    k = str(k)
    num = k[1]

    # jesli w wyniku otrzymam 10, to na sztywno ustawiam 0
    control_num_final = 10 - int(num)
    if control_num_final == 10:
        control_num_final = 0

    pesel_final = str(year) + str(month) + str(day) + str(pppp) + str(control_num_final)
    return pesel_final