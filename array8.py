def find_error_nums(nums):
    duplicate = -1
    missing = -1

    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] *= -1
        else:
            duplicate = abs(num)

    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1
            break

    return [duplicate, missing]

nums = [1, 2, 2, 4]
print(find_error_nums(nums))
