                                             ########question###########
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

                                   #########code########
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

                       ##########explaination#########
i is the first number and j is second number as the sum should be equal to target number we should take one number and search for the other number which
 when added with the first number gives the target number the for loop continues like this 
