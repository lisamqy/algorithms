'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.'''

class Solution:
    def firstUniqChar(self, s:str) -> int:
        # put everything in dictionary for faster lookup
        dict = {}
        for letter in s:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
        # now we check for if unique exist in our dict
        for idx, letter in enumerate(s):
            if dict[letter] == 1:
                return idx
        return -1


# Time = O(n) n depending on the number of loops