"""
-- Part Two ---

An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

    112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
    123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
    111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).

How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle input is still 271973-785961.
"""

low = 271973
high = 785961

def is_increasing(number):
    if int(number[0]) <= int(number[1]) and int(number[1]) <= int(number[2]) and int(number[2]) <= int(number[3]) and int(number[3]) <= int(number[4]) and int(number[4]) <= int(number[5]):
        return True
    return False


def check_larger_repeating(number):
    nums = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0
    }
    for i in number:
        nums[i] += 1
    for i in nums:
        if nums[i] == 2:
            return True
    return False

count = 0

for i in range(low, high+1):
    number = str(i)
    if is_increasing(number) and check_larger_repeating(number):
        count+=1

print(count)

