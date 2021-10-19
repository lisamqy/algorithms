'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.'''

# O(n) Time and space solution using Bucket Sort

class Solution:
    def topKFrequent(self, nums, k):
        # use a hashmap to count the occurences of each value
        count = {}
        # create a list of empty lists for buckets for the possible frequencies (range of len of our nums list plus 1)
        # the value would be the number from our list that occurred that many times
        freq = [[] for i in range(len(num) + 1 )]

        # iterate through the given nums list and count how many times each item has occurred
        for n in nums:
            # if current number does not exist in our dict, then we add 1+0 else we increment old number by 1
            count[n] = 1 + count.get(n, 0)
        # now we iterate through our counted values in our dict by getting the dict's key:value pair
        for n, c in count.items():
            # "this value 'n' occurs exactly 'c' number of times"
            freq[c].append(n)
        
        result = []

        # now we iterate through the freq list backwards
        # aka going from the last index(-1) until the the first(0), in descending order(-1)
        for i in range(len(freq) -1, 0, -1):
            # iterate through every value since our i is a sublist that could be empty or have some values
            for val in freq[i]:
                result.append(val)
                # get enough values to match the given k value
                if len(result) == k:
                    return result