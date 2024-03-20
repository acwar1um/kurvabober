import random                                                                    
while True:
    songs = []
    name = input()
    if name == '0':
        print('К сожалению, ничего не удалось найти')
        break
    else:
        with open('songs.csv', encoding='utf8') as f:
            for a in f:
                s = [i for i in a.split(';')]
                if s[1] == name:
                    songs.append(s[2])
            print(f'У {name} найдена песня: {random.choice(songs)}')