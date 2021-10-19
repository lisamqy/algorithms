'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

'''

# Brute force method -> produce all pairs, sort them by sum and then return the first k

# More efficient method;
# Time complexity O(n * log k), where n is len(nums1).

import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k): 
        l1, l2 = len(nums1), len(nums2)
        if not nums1 or not nums2:
            return []

        # heap: list of tuples (nums1[i] + nums2[j], i, j), which is initialized with j = 0 and i = 0, 1, ..., len(nums1) - 1
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(l1)]
        heapq.heapify(heap)
        result = [] 
        # In the while loop...
        while k > 0 and heap:
            # ...we pop the smallest element (nums1[i] + nums2[j], i, j) from the heap
            s, i ,j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < l2:
                # ...and push (nums1[i] + nums2[j+1], i, j+1) to the heap if it exists.
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        
        return result