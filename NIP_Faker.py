import random


def nip():

    # losuję 3 pierwsze cyfry dla urzedu skarbowego
    us_number = random.randint(101, 998)
    if isinstance(us_number, int):
        us_number += 1

    # losuje kolejnych 6 cyfr peselu
    random_number = str(us_number) + str(random.randint(111111, 999999))

    # sprawdzanie sumy kontrolnej
    control_sum = [int(i) for i in str(random_number)]

    # sprawdzanie wagi dla sumy kontrolnej
    balance_list = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    result = [a * b for a, b in zip(control_sum, balance_list)]
    list(map(int, result))
    modulo = sum(result) % 11
    nip_final = str(random_number) + str(modulo)
    return nip_final
