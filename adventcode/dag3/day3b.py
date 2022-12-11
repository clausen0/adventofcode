with open('./dag3/input.txt', 'r') as f:
    lines = f.readlines()
    rucksacks = [entry.strip() for entry in lines]

rucksack_sum = 0 
while len(rucksacks) > 0:
    first_half = set(rucksacks.pop())
    second_half = set(rucksacks.pop())
    third_half = set(rucksacks.pop())

    overlap_char = ((first_half.intersection(second_half)).intersection(third_half)).pop()

    if overlap_char.isupper():
        rucksack_sum += ord(overlap_char) - ord('A') + 27
    else:
        rucksack_sum += ord(overlap_char) - ord('a') + 1

rucksack_sum
print(rucksack_sum)

# print(first_half)
# print(second_half)