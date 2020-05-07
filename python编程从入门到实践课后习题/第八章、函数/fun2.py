def city_country(city,country):
    location = city + ", " + country
    return location

print(city_country('hangzhou','china'))

def make_album(singer,album_name,number=0):
    album = {'singer':singer,'name':album_name}
    if number:
        album['numbers'] = number
    return album

musician1 = make_album('jayzhou','mojiezuo',3)
musician2 = make_album('tyc','nevermore')
musician3 = make_album('shuaige','hahahah')
print(musician1)
print(musician2)
i = 0
musician = []
while True:
    print("\nplz Enter a album:")
    print("(enter 'q' at any time to quit)")
    sin = input("singer's name is:")
    if sin == 'q':
        break
    album_name = input("album_name is:")
    if album_name == 'q':
        break

    musician.append(make_album(sin,album_name))
    print(musician[i])
    i += 1
