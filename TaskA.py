"""
                Задачка
Победитель популярной в Берляндии карточной игры «Берлоггинг» определяется по следующим правилам.
Если на момент окончания игры существует только один игрок, набравший максимальное количество очков,
то он и становится победителем. Ситуация осложняется, если таких игроков несколько. Каждый кон игры некоторый
игрок выигрывает или проигрывает некоторое количество очков. В записи о ходе игры это обозначается
строкой «name score», где name это имя игрока, а score целое число обозначающее количество заработанных очков
данным игроком. Если score — отрицательное число, это обозначает, что игрок проиграл в этом коне. Т
ак вот, если на конец игры несколько игроков набрали максимум очков (пусть это число равно m), то выигрывает тот из них,
кто первым набрал как минимум m очков. Перед началом игры у каждого игрока 0 очков. Гарантируется, что на момент
окончания игры хотя бы у одного игрока положительное число очков.
"""
listPerson = []
mapPerson = {}
topMapPerson = {}
max_value = 0


def insert(name: str, value: int):
    listPerson.append({"name": name, "value": value})
    if name in mapPerson:
        mapPerson[name] = mapPerson[name] + value
    else:
        mapPerson[name] = value
    return


def runSolution():
    global max_value
    n = int(input())
    for index in range(0, n):
        strMas = input().split(" ")
        insert(name=strMas[0], value=int(strMas[1]))

    for key in mapPerson:
        if max_value < mapPerson[key]:
            max_value = mapPerson[key]

    for key in mapPerson:
        if max_value == mapPerson[key]:
            topMapPerson[key] = 0

    winner = ""
    for i in range(0, len(listPerson)):
        if listPerson[i]["name"] not in topMapPerson:
            continue
        topMapPerson[listPerson[i]["name"]] = topMapPerson[listPerson[i]["name"]] + listPerson[i]["value"]
        if topMapPerson[listPerson[i]["name"]] >= max_value:
            winner = listPerson[i]["name"]
            break

    print(winner)


if __name__ == '__main__':
    runSolution()

# 3
# qwe 2
# qwerty 5
# qwe 3
# answer = qwerty

# 3
# mike 10
# mike -9
# tom 5

# 5
# bob 10
# bob 20
# bob -25
# mike 10
# bob 5

# 5
# q -5
# q -6
# w -2
# e 8
# e -100

# 5
# qwe 100
# asd 50
# zxc 60
# qwe -60
# zxc -10
# answer asd