#QUESTION
2091. Removing Minimum and Maximum From Array
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed array of distinct integers nums.

There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.

A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.

Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

#CODE
class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        from_left = right + 1
        from_right = n - left
        from_both = (left + 1) + (n - right)

        return min(from_left, from_right, from_both)
        
