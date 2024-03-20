with open('songs.csv', encoding='utf8') as f:
    lllll = f.readline()
    russian_artists = []
    foreign_artists = []
    for a in f:
        s = [i for i in a.split(';')]
        for ss in s[1]:
            if ss in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                russian_artists.append(s[1])
                break 
            else:
                foreign_artists.append(s[1])
                break
    r = len(set(russian_artists))
    f = len(set(foreign_artists))
    print(f'Количество российских исполнителей: {r} \nКоличество иностранных исполнителей: {f}')
    with open('russian_artists.txt', 'w', encoding='utf8') as f:
        for i in set(russian_artists):
            f.write(f'{i} \n')
    with open('foreign_artists.txt', 'w', encoding='utf8') as f:
        for i in set(foreign_artists):
            f.write(f'{i} \n')