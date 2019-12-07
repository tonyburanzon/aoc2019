"""
--- Day 4: Secure Container ---

You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 271973-785961.
"""

low = 271973
high = 785961

def is_increasing(number):
    if int(number[0]) <= int(number[1]) and int(number[1]) <= int(number[2]) and int(number[2]) <= int(number[3]) and int(number[3]) <= int(number[4]) and int(number[4]) <= int(number[5]):
        return True
    return False

def duplicate(number):
    for i in range(len(number)-1):
        if number[i] == number[i+1]:
            return True
    return False

count = 0

for i in range(low, high+1):
    number = str(i)
    if is_increasing(number) and duplicate(number):
        count+=1

print(count)

