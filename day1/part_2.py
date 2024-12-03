# https://adventofcode.com/2024/day/1


def count_same_numbers(data: list[int], number: int) -> int:
    count = 0
    for i in data:
        if i == number:
            count += 1
    return count


with open("part_1_2.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

list_a, list_b = [], []

for line in lines:
    line = line.strip()
    nums = line.split()
    list_a.append(int(nums[0]))
    list_b.append(int(nums[1]))

count = 0

for i in list_a:
    same_num = count_same_numbers(list_b, i)

    if same_num == 0:
        continue

    similarity_score = i * same_num
    count += similarity_score

print(count)