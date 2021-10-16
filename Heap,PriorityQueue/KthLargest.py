'''Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.'''

'''
Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
'''

import heapq

'''
Create a pq - keep it only having the k-largest elements by popping off small elements.
With only k elements, the smallest item (self.pool[0]) will always be the kth largest.
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for num in nums:
            self.add(num)
        
    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)

        # if after adding the new item causes the heap size to increase beyond k,
        # pop out the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # return root element aka index 0
        return self.heap[0]

     
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)