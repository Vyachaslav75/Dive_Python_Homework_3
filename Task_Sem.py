
hiking_team = {
    'Алексей':('Палатка', 'Термос', 'Веревка', 'Спальник', 'Фонарь', 'Топор'),
    'Сергей':('Палатка', 'Вода', 'Крупа', 'Спальник', 'Фонарь', 'Куртка'),
    'Александр':('Спальник', 'Фонарь', 'Топор', 'Куртка', 'Нож', 'Вода', 'Хлеб')
}

res=set()
for item in hiking_team:
    if len(res)>0:
        res=res & set(hiking_team[item])
    else:
        res=set(hiking_team[item])
print(f'Есть у всех {res}')

for item in hiking_team:
    res=set(hiking_team[item])
    for item1 in hiking_team:
        if item != item1:
            res = res - set(hiking_team[item1])
    print(f'Есть тоько у {item}: {res}')
    
for item in hiking_team:
    res={}
    for item1 in hiking_team:
        if item != item1:
            if len(res)>0:
                res=res & set(hiking_team[item1])
            else:
                res=set(hiking_team[item1])
    res = res - set(hiking_team[item])
    print(f'У {item} нет {res}. У остальных есть.')
