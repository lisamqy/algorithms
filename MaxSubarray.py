'''Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

'''

# sliding window problem; solution using linear time
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initailize our max sub array to equal to the 0th index of the given nums list
        # NOTE: we can't just make it equal to 0 since the given list could include negatives
        maxSub = nums[0]
        # initialize a current sum set to 0 so it can be updated later on
        curSum = 0

        # iterate through the given nums list
        for n in nums:
            # if at any point the prefix/current sum is negative; just reset it back to 0
            if curSum < 0:
                curSum = 0
            # dont forget to update our current sum 
            curSum += n
            # since this curSum could be our potential maximum, update the maxSub
            maxSub = max(maxSub, curSum)

        return maxSub