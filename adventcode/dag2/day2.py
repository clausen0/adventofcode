with open('./dag2/input.txt', 'r') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

map_input = {'A': 'Stein', 'B': 'Papir', 'C': 'Saks', 'X': 'Stein', 'Y': 'Papir', 'Z': 'Saks'}
poeng_per_form = {'Stein': 1, 'Papir': 2, 'Saks': 3}
poeng_per_situasjon = {'Tap': 0, 'Uavgjort': 3, 'Seier': 6}

def poeng_per_runde(round_string):
    motstander_tegn = map_input[round_string[0]]
    mitt_tegn = map_input[round_string[2]]

    if motstander_tegn == mitt_tegn:
        return poeng_per_situasjon['Uavgjort'] + poeng_per_form[mitt_tegn]
    elif (motstander_tegn,  mitt_tegn) in [('Papir', 'Stein'), ('Stein', 'Saks'), ('Saks', 'Papir')]:
        return poeng_per_situasjon['Tap'] + poeng_per_form[mitt_tegn]
    else:
        return poeng_per_situasjon['Seier'] + poeng_per_form[mitt_tegn]

# print(poeng_per_runde(rounds[7]))
print(sum([poeng_per_runde(round_string) for round_string in rounds]))