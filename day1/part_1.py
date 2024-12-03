# https://adventofcode.com/2024/day/1


def get_smallest(data: list[int]) -> tuple[int, int]:
    smallest = data[0]
    smallest_index = 0
    for i in range(1, len(data)):
        if data[i] < smallest:
            smallest = data[i]
            smallest_index = i
    return smallest, smallest_index


with open("part_1.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

list_a, list_b = [], []

for line in lines:
    line = line.strip()
    nums = line.split()
    list_a.append(int(nums[0]))
    list_b.append(int(nums[1]))

length = len(list_a)

count = 0
while True:
    if len(list_a) == 0:
        break

    smallest_a = get_smallest(list_a)
    smallest_b = get_smallest(list_b)

    diff = abs(smallest_a[0] - smallest_b[0])
    count += diff

    list_a.pop(smallest_a[1])
    list_b.pop(smallest_b[1])


print(count)
