with open('./dag2/input.txt', 'r') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

map_input = {'A': 'Stein', 'B': 'Papir', 'C': 'Saks', 'X': 'Tap', 'Y': 'Uavgjort', 'Z': 'Seier'}
poeng_per_form = {'Stein': 1, 'Papir': 2, 'Saks': 3}
poeng_per_situasjon = {'Tap': 0, 'Uavgjort': 3, 'Seier': 6}

def poeng_per_runde(round_string):
    motstander_tegn = map_input[round_string[0]]
    mitt_mål = map_input[round_string[2]]

    if (motstander_tegn, mitt_mål) in [('Stein', 'Uavgjort'), ('Papir', 'Tap'), ('Saks', 'Seier')]:
        return poeng_per_situasjon[mitt_mål] + poeng_per_form['Stein']
    elif (motstander_tegn, mitt_mål) in [('Stein', 'Seier'), ('Papir', 'Uavgjort'), ('Saks', 'Tap')]:
        return poeng_per_situasjon[mitt_mål] + poeng_per_form['Papir']
    else:
        return poeng_per_situasjon[mitt_mål] + poeng_per_form['Saks']


# print(poeng_per_runde(rounds[7]))
print(sum([poeng_per_runde(round_string) for round_string in rounds]))