"""
Билеты на метро

Билет на одну поездку в метро стоит 15 рублей, билет на 5 поездок стоит 70 рублей, билет на 10 поездок стоит 125 рублей,
билет на 20 поездок стоит 230 рублей, билет на 60 поездок стоит 440 рублей. Пассажир планирует совершить n поездок.
Определите, сколько билетов каждого вида он должен приобрести, чтобы суммарное количество оплаченных поездок было
не меньше n, а общая стоимость приобретенных билетов – минимальна.

    Входные данные
    Дано одно число n - количество поездок.

    Выходные данные
    Выведите пять целых чисел, равные необходимому количеству билетов на 1, на 5, на 10, на 20, на 60 поездок.
    Если для какого-то данного n существует несколько способов приобретения билетов одинаковой стоимости,
    необходимо вывести ту комбинацию билетов, которая дает большее число поездок.
"""

n = int(input())
price = {1: [1, 15], 2: [5, 70], 3: [10, 125], 4: [20, 230], 5: [60, 440]}
res = [0, 0, 0, 0, 0]


def get_sum(mas_sum):
    price_res = 0
    for i in range(len(mas_sum)):
        price_res = price_res + mas_sum[i] * price[i + 1][1]
    return price_res


def run():
    new_n = n
    for i in range(5, 0, -1):
        res[i - 1] = new_n // price.get(i)[0]
        new_n = new_n % price[i][0]

    sum_res = get_sum(res)
    temp_res = [x for x in res]

    for i in range(1, 5, 1):
        temp_res[i - 1] = 0
        temp_res[i] = temp_res[i] + 1
        mas_write = [x for x in temp_res]

        ticket_price = get_sum(mas_write)

        if (ticket_price > sum_res) or (ticket_price == sum_res and sum(mas_write) > sum(res)):
            continue

        sum_res = ticket_price
        for i in range(len(mas_write)):
            res[i] = mas_write[i]


run()

print(*res, sep=' ')
