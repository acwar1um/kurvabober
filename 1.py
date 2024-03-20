import datetime
with open('songs.csv', encoding='utf8') as f:
    llll = f.readline()
    for a in f:
        s = [i for i in a.split(';')]
        k = s[-1].replace('\n', '').split('.')
        if datetime.date(2002,1,1) >= datetime.date(int(k[2]), int(k[1]), int(k[0])):
            print(f'{s[2]} - {s[1]} - {s[0]}')