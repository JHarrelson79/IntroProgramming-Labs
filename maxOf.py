import math


    
def maxOf(nums):
    maxSoFar = -math.inf
    for i in range( len(nums)):
        nextNum = nums[i]
        if nextNum > maxSoFar:
            maxSoFar = nextNum
    return maxSoFar

scores = [91,84,75,94,67]

print("The max score is", maxOf(scores))  