print("Начался восьмичасовой рабочий день.")
count_hour = 1
go_store = False
count_Tasks = 0
while count_hour < 9:
    print(f'{count_hour}-й час')
    count_work = int(input("Сколько задач решит Максим? "))
    count_Tasks += count_work
    call_wife = int(input("Звонит жена, взять трубку? (1 - да, 0 - нет) "))
    if call_wife == 1:
        go_store = True
    count_hour += 1
print(f"Рабочий день закончился. Всего задач выполнено {count_Tasks}")  
if go_store:
    print("Необходимо зайти в магазин")
