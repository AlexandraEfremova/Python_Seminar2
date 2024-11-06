all_cards = int(input("Введите количество карточек: "))
sum_all_cards = 0
for card in range(1, all_cards + 1):
    sum_all_cards += card
for card in range(all_cards - 1):
    rem_card = int(input("Номер карточки, которая ещё есть: "))
    sum_all_cards -= rem_card
print(f"Номер карточки, которая потерялась {sum_all_cards}")