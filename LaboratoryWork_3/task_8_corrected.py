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

while money_capital >= spend:
    money_capital = money_capital + salary - spend
    spend = (1 + increase) * spend
    month += 1

print(month)
