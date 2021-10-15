'''Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.'''

# Brute Force method would be O(n^2) bc we have n^2 diff sub arrays inside of the array


# Using hashmap for O(n) time and space result
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # create a counter so we can increment whenever we find a subarray sum that equals to k
        count = 0
        # store current sum that's initially set to 0
        current_sum = 0
        # hashmap with a base case of 0(key) with a count of 1(value) since we have a single prefix sum that sums up to 0
        prefix_sum = { 0 : 1 } 
        
        # iterate through each value in the given list 
        # NOTE: ex List: [3, 4, 7, 2, -3, 1, 4, 2] , k = 7
        for n in nums:
            
            # add to current sum
            # NOTE: [3, 7, 14, 16, 13, 14, 18, 20]; first current_sum is 3
            current_sum += n

            # and get the difference to see check if the current subarray can get a sum equal to k
            # NOTE: diff = 3 - 7; diff => -4
            diff = current_sum - k

            # add to our count if we do find else add 0
            # NOTE: -4 is not in our diff so we add 0 to count
            count += prefix_sum.get(diff, 0)

            # update our prefix_sum dict
            # NOTE: we add 3 to our prefix_sum dict; prefix_sum[3] = 1 + 0
            prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum, 0)

        return count