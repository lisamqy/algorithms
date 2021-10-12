'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.'''

'''An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

class Solution:
    def isValid(self, str): # returns bool
        # initiate a stack
        parens_stack = []
        # iterate through given string
        for char in str:
            # check if they are open parens
            # append the corresponding closed parens into our stack
            if char == '(':
                parens_stack.append(')')
            elif char == '{':
                parens_stack.append('}')
            elif char == '[':
                parens_stack.append(']')
            # otherwise it must be a closing parens or None
            # return false if char does not match top of our stack or if stack still empty
            elif len(parens_stack) == 0 or char != parens_stack.pop():
                return False
        # by the end of the loop everything from our stack should be popped off if all parens were valid
        return len(parens_stack) == 0


# Time = O(n) with n being the number of characters in the given string
# Space = O(n) bc worse case its just going to be a very long string