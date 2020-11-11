"""
How many minimum numbers from fibonacci series are required such that sum of numbers should be equal to a given Number N?
Note : repetition of number is allowed.

Example:

N = 4
Fibonacci numbers : 1 1 2 3 5 .... so on
here 2 + 2 = 4 
so minimum numbers will be 2 
"""


class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        l = [1,1]
        while l[-1]<A:
            l.append(l[-1]+l[-2])
        rem = A
        count=0
        while rem:
            if l[-1]>rem:
                l.pop()
            else:
                rem -= l[-1]
                count += 1
        return count
    
