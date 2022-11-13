money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month_ = 0  # количество месяцев, которое можно прожить
delta_ = abs(salary - spend)
while (money_capital - delta_) > 0:
    money_capital = money_capital - delta_
    month_ += 1
    delta_ = delta_ + increase * spend
print(month_)


# TODO Оформить решение
