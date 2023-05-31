def move_zeroes(nums):
    pos = 0

    for num in nums:

        if num != 0:
            nums[pos] = num
            pos += 1

    for i in range(pos, len(nums)):
        nums[i] = 0

nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)
