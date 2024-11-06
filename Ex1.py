n = int(input("Введите число от -100 до 100: "))
pos_num = 0
neg_num = 0
while n != 0:
    if n > 0:
        pos_num += 1
    else:
        neg_num += 1
    n = int(input("Введите число от -100 до 100: ")) 
print(f"Количество позитивных оценок {pos_num}")
print(f"Количество негативных оценок {neg_num}")