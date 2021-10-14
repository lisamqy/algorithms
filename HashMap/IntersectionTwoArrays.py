'''Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.'''

class Solution:
    def intersection(self, nums1:List[int], nums2: List[int]) -> List[int]:

        # store only unique numbers
        nums1 = set(nums1)
        nums2 = set(nums2)
        # use the &(bitwise AND) operator to return only the nums with the same bits from the two lists
        return list(nums1 & nums2)