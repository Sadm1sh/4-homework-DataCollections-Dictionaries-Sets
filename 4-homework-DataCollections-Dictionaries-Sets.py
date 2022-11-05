#####Задание №1
from pprint import pprint
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
g_logs = []
for list in geo_logs:
    for visit in list.values():
        for russia in range(len(visit)):
            if visit[russia] == "Россия":
                g_logs.append(list)
pprint(g_logs)
#####Задание №2
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
ids_u= set()
for x in ids.values():
    for i in set(x):
        ids_u.add(i)
print(ids_u)
#####Задание №3
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
checklist = {}
for query in queries:
    word = query.split()
    if len(word) in checklist:
        checklist[len(word)] += 1
    else:
            checklist[len(word)] = 1
for key, value in sorted(checklist.items()):
    procent = round(value / len(queries) * 100, 1)
    print(f"Поисковых запросов из {key} слов: {procent}% [{value}запр.]")
  #####Зажание №4
stats = {'yandex': 120, 'vk': 115, 'google': 99, 'email': 21, 'ok': 98}
#ищет максимальное значение stats, выводит ключ
max_stats = max(stats, key=stats.get)
print(max_stats)
####Задание №5
def slovar(spisok:list) -> dict:
    if len(spisok) == 1:
        return spisok[0]
    return {spisok[0]: slovar(spisok[1:])}


spisok = ['2018-01-01', 'yandex', 'cpc', 100]
print(slovar(spisok))