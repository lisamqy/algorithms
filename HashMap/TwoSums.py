'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.'''

# Brute Force Solution O(n^2) using two for loops
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through all the numbs except the last one
        for i in range(len(nums)-1):
            # loop through all indices again except index i
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return([i,j])

# HashMap Solution O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create empty dict to store/track the numbers
        seen = {}
        # get both index and element using enumerate function
        for i, num in enumerate(nums):
            # check if the difference between the target and num is in dict
            # if so, return that num/key's value along with the current num's i/index
            if target - num in seen:
                return [seen[target - num], i]
            # otherwise we add that number along with it's index as key:value pair into dict
            elif num not in seen:
                seen[num] = i
            
                