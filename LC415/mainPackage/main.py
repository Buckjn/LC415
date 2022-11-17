'''
Created on Nov 17, 2022

@author: 15137
'''

#This is our entry point to the test code
#We will test the Solution Class for LeetCode problem 415
#Prof provided the solution code. How to link to LeetCode???

from solutionPackage import *

#instantiate an object of type Solution
mySolution = Solution()
result = mySolution.addStrings("123","456")
print(result)
#do a test that will fail
result = mySolution.addStrings("aaa","bbb")
print(result)
result = mySolution.addStrings("-123","456")
print(result)

result = mySolution.addStrings("123.5","456.1")
print(result)
result = mySolution.addStrings("123a","456b")
print(result)
