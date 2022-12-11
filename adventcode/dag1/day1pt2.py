with open('./dag1/input.txt', 'r') as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]

sum_elfes = []
currentsum = 0
for entry in calories:
    if entry != '':
        currentsum += int(entry)
    elif entry == '':
        sum_elfes.append(currentsum)
        currentsum = 0
sum_elfes.append(currentsum)

sum_elfes.sort(reverse=True)
print(sum_elfes[0]+sum_elfes[1]+sum_elfes[2])