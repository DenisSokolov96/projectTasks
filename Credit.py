# выдача кредита
# расчет платежа в месяц при дифференцированной выплате:
def p_t(s, n, k, t):
    return (s / n) + (s - (t - 1) * s / n) * k / 1200


# расчет ежемесячного платежа при аннуитетной выплат:
def ann(s, n, k):
    ka = k / 1200
    return ((ka * (1 + ka) ** n) / (((1 + ka) ** n) - 1)) * s


if __name__ == "__main__":
    s = int(input())  # кредеит
    n = int(input())  # месяц
    k = int(input())  # процент
    bank_summa_dif = 0
    bank_summa_ann = 0
    for t in range(1, n + 1):
        summa_dif = p_t(s, n, k, t)
        summa_ann = ann(s, n, k)
        bank_summa_dif = bank_summa_dif + summa_dif
        bank_summa_ann = bank_summa_ann + summa_ann
        print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб" % (t, summa_dif, summa_ann))
    print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб" % (bank_summa_dif - s, bank_summa_ann - s))
