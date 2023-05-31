def plus_one(digits):
    carry = 1

    for i in range(len(digits) - 1, -1, -1):
        digit_sum = digits[i] + carry
        if digit_sum < 10:
            digits[i] = digit_sum
            carry = 0
        else:
            digits[i] = 0
            carry = 1

    if carry == 1:
        digits.insert(0, 1)
    return digits

digits = [1, 2, 3]
print(plus_one(digits))
