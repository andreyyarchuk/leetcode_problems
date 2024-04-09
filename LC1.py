#   Two Sum
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.


def twoSum(nums, target):
    list = []
    for i in range(len(nums)):
        current_sum = 0
        current_num = nums[i]
        for j in range(len(nums)):
            if i != j:
                comparison_num = nums[j]
                current_sum = current_num + comparison_num
                if current_sum == target:
                    return [i, j]


print('hello')