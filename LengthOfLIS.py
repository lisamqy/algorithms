'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.'''

'''
A subsequence is a sequence that can be derived from an array by deleting some or no elements without 
changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

'''

# DP style solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # cache the repeated work
        # so everything longest increasing subsequence start at every index is initially set to 1 (so we can update it with the max later on)
        LIS = [1] * len(nums)

        # iterate through every index in the range of our input array in reversed order
        for i in range(len(nums) -1, -1, -1):
            # another nested loop to go through the nums after the i index
            for j in range(i + 1, len(nums)):
                # check if value at i is less than the value at j; since j comes after it and we want it to be in increasing order/subsquence
                if nums[i] < nums[j]:
                    # if so, update the LIS at index i
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

# Time: O(n^2) due to the nested loops