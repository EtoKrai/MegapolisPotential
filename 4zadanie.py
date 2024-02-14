import csv
'''
С помощью данной программы можно подсчитать количество русских и иностранных исполнителей
'''
with open('songs.csv','r',encoding='utf-8') as file, open('russian_artists.txt','w',encoding='utf-8') as russia, open('foreign_artists.txt','w',encoding='utf-8') as mir:
    reader=csv.reader(file,delimiter=';')
    w1=csv.writer(russia)
    w2=csv.writer(mir)
    answer=list(reader)[1:]
    russian=[]
    foreign=[]
    text=''
    for line in answer:
        if 'а' in line[1] or 'у' in line[1] or 'е' in line[1] or 'о' in line[1] or 'э' in line[1] or 'я' in line[1] or 'и' in line[1] or 'ю' in line[1] and line[1] not in russian:
            russian.append(line[1])
        else:
            if line[1] not in foreign and line[1]!='unknown':
                foreign.append(line[1])
    print(f'Количество российских исполнителей: {len(russian)}')
    print(f"Количество иностранных исполнителей: {len(foreign)}")
    for i in range(len(russian)):
        w1.writerow(russian[i])
    for i in range(len(foreign)):
        w2.writerow(foreign[i])

