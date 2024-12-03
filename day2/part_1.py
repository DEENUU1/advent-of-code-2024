def is_safe_report(numbers):
    nums = [int(n) for n in numbers]

    is_increasing = nums[1] > nums[0]

    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if is_increasing and diff <= 0:
            return False
        if not is_increasing and diff >= 0:
            return False

    return True


with open("part_1_2.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

total_safe = sum(1 for line in lines if is_safe_report(line.strip().split()))

print(total_safe)