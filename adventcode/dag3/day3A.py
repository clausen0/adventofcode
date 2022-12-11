with open('./dag3/input.txt', 'r') as f:
    lines = f.readlines()
    rucksacks = [entry.strip() for entry in lines]

rucksack_sum = 0 
for rucksack in rucksacks:
    first_half = set(rucksack[:len(rucksack)//2])
    second_half = set(rucksack[len(rucksack)//2:])
    overlap_char = (first_half.intersection(second_half)).pop()

    if overlap_char.isupper():
        rucksack_sum += ord(overlap_char) - ord('A') + 27
    else:
        rucksack_sum += ord(overlap_char) - ord('a') + 1

rucksack_sum
print(rucksack_sum)

# print(first_half)
# print(second_half)