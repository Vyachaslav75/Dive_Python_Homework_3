things = {
    'Палатка': 5,
    'Термос': 2,
    'Веревка': 1,
    'Спальник': 2,
    'Тушенка': 6,
    'Вода': 3,
    'Куртка': 1,
    'Топор': 2,
    'Фонарь': 1,
    'Крупа': 3
}
#backpack_weigth = 15
backpack_weigth = int(input('Введите грузоподъемность рюкзака: '))
backpack = []

for item in things:
    if backpack_weigth - things[item] >=0:
        backpack.append(item)
        backpack_weigth -= things[item]
print(backpack)