import random


def nip():
    us_number = random.randint(101, 998)
    if isinstance(us_number, int):
        us_number += 1

    random_number = str(us_number) + str(random.randint(111111, 999999))
    control_sum = [int(i) for i in str(random_number)]
    balance_list = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    result = [a * b for a, b in zip(control_sum, balance_list)]
    wynik = result / 11
    if wynik == 10:
        wynik += 1
    results = list(map(int, result))
    k = sum(results)
    k = str(k)
    num = k[1]
    nip_final = str(results) + str(num)
    return nip_final
print(nip())