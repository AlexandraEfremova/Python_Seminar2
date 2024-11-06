sum_salary_in_year = 0
month = 1
while month < 13:
    print(f"Сейчас {month}-й месяц")
    salary_in_month = int(input("Введите зарплату работника за текущий месяц "))
    sum_salary_in_year += salary_in_month
    month += 1
avg_salary = sum_salary_in_year / 12
print(f"Средняя зарплата сотрудника за год: {avg_salary}")