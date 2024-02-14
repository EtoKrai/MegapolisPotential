import csv

'''
Поиск исполнителся и вывод его песни
'''
vvod = input('Введите имя артиста: ')
while True:
    if vvod == '0':
        break
    with open('songs.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        answer = list(reader)[1:]
        count = {}
        for streams, artist_name, track_name, date in answer:
            count[artist_name] = count.get(artist_name, '') + track_name
        if vvod not in count or vvod == 'unknown':
            print("К сожалению, ничего не удалось найти")
            vvod = input('Введите имя артиста: ')
        else:
            print(f'У артиста найдена песня: {count[vvod]}')
            vvod = input('Введите имя артиста: ')
    if vvod == '0':
        break