count_boys = int(input('Введите кол-во мальчиков: '))
count_girls = int(input('Введите кол-во девочек: '))
answer = ''
if (count_boys > 2 * count_girls) or (count_girls > 2 * count_boys):
    print('Нет решения')
elif count_boys >= count_girls:
    extra = count_boys - count_girls 
for BGB in range(extra):
    answer += 'BGB'
for BG in range(count_girls - extra):
    answer += 'BG'
else:
    extra = count_girls - count_boys 
for GBG in range(extra):
    answer += 'GBG'
for GB in range(count_boys - extra):
    answer += 'GB'
print(answer)