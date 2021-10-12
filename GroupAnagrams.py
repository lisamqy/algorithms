'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.'''

from collections import defaultdict


# time complexity is O(n * k + log k) since its sorted
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a lookup for a defaultdict with list as our value
        # NOTE: defaultdict will "default" a value if that key has not been set yet. 
        # NOTE: If you use a regular dictionary, you'd have to check to see if that key exists (and if it doesn't, set it to what you want.)
        result = defaultdict(list)
        # iterate through list of strs
        for str in strs:
            # check if our sorted str key is already in dict
            # NOTE: using sorted() on a str will return a list of sorted charas so we have to join it back
            sorted_str = ''.join(sorted(str))
            # add the sorted str into our dict and append to it the unsorted str
            result[sorted_str].append(str)

        return result.values()

# Using dict.get()
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a lookup for a defaultdict with list as our value
        result = {}
        # iterate through list of strs
        for str in strs:
            # turn the sorted letters of that str into tuple to use as key
            sorted_str_tuple = tuple(sorted(str))
            # either create a new key:value pair for the sorted str tuple or 
            # add a value(unsorted str) to an existing sorted str tuple
            result[sorted_str_tuple] = result.get(sorted_str_tuple, []) + [str]
        # return as a list of lists
        return list(result.values())


# Using ascii 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for letter in str:
                # map a to 0...z to 25 by taking difference of current letter's ascii value and ascii value of 'a' using ord()
                # then add 1 to the index number
                count[ord(letter) - ord('a')] += 1
            # add to dict using tuple for keys since they're hashable
            result[tuple(count)].append(str)

        return result.values()