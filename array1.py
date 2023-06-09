def two_sum(nums, target):

    complement_dict = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in complement_dict:
            return [complement_dict[complement], i]
        else:
            complement_dict[num] = i

    return []

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
