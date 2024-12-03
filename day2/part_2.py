def is_safe_sequence(nums):
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


def is_safe_report_with_dampener(numbers):
    nums = [int(n) for n in numbers]

    if is_safe_sequence(nums):
        return True

    for i in range(len(nums)):
        dampened_nums = nums[:i] + nums[i + 1:]
        if is_safe_sequence(dampened_nums):
            return True

    return False


with open("part_1_2.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

total_safe = sum(1 for line in lines if is_safe_report_with_dampener(line.strip().split()))

print(f"Number of safe reports with Problem Dampener: {total_safe}")