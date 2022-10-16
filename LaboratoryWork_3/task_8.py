"""
Условие задачи:
Имеется финансовая подушка безопасности
money_capital руб. Ежемесячная зарплата
составляет salary рублей,
а расходы на проживание превышают ее и
составляют spend руб. в месяц. Рост цен
ежемесячно увеличивает расходы на 5%.

Определить, сколько можно прожить, используя
только подушку и зарплату.
"""

money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

sum_for_life = money_capital + salary - spend  # сумма на конец месяца

counter = 1  # так как первый месяц уже прожили (sum_for_life > 0)
while True:
    spend = (1 + increase) * spend
    sum_for_life = sum_for_life + salary - spend
    counter += 1
    if sum_for_life < 0:
        counter -= 1
        """
        Так как мы в текущем месяце уже прибавили к
        счётчику единицу, несмотря на то, что текущий
        месяц мы не прожили (sum_for_life < 0)
        """
        break

month = counter
print(month)
