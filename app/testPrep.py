##Write a function productExceptSelf(nums) that takes an array nums of n integers and returns an array output
##such that output[i] is equal to the product of all the elements of nums except nums[i], without using division.
from typing import List
def productExceptSelf(nums: List[int]):
    product_array = []
    product = 1
    for (index, value) in enumerate(nums):
        product = 1
        # First iteration which will go one by one
        for (i, v) in enumerate(nums):
            if i  == index:
                continue
            product = product * v

        product_array.append(product)
    return product_array


x = productExceptSelf([1,2,3])
print(x)

# Given an array arr[] of positive numbers, the task is to find the maximum sum of a subsequence such that no
# two numbers in the sequence should be adjacent in the array.


# Function to find the maximum sum
def rec(nums, idx):
    if idx >= len(nums):
        return 0
    return max(nums[idx] + rec(nums, idx + 2), rec(nums, idx + 1))

# Given array of [1,3,5] list all combinations you can form N using their sum

def comb(n):
    if n < -1:
        return 0
    if n == 1:
        return 1
    return comb(n - 1) + comb(n - 3) + comb(n - 5)

# Lowest cost traversal in a matrix
import sys
def minCost(cost, m, n):
    if (n < 0 or m < 0):
        return sys.maxsize
    elif (m == 0 and n == 0):
        return cost[m][n]
    else:
        return cost[m][n] + min(minCost(cost, m-1, n-1),
                                 minCost(cost, m-1, n),
                                minCost(cost, m, n-1))

# A utility function that returns minimum of 3 integers */


def min(x, y, z):
    if (x < y):
        return x if (x < z) else z
    else:
        return y if (y < z) else z


# Driver code
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(minCost(cost, 2, 2))




# A recursive solution for subset sum
# problem


# Returns true if there is a subset
# of set[] with sun equal to given sum
def isSubsetSum(set, n, sum):
 
    # Base Cases
    if (sum == 0):
        return True
    if (n == 0):
        return False
 
    # If last element is greater than
    # sum, then ignore it move to the next one
    if (set[n - 1] > sum):
        return isSubsetSum(set, n - 1, sum)
 
    # Else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubsetSum(set, n-1, sum-set[n-1])



# Recursive Python3 program for
# coin change problem.

# Returns the count of ways we can sum
# coins[0...n-1] coins to get sum "sum"


def count(coins, n, sum):

    # If sum is 0 then there is 1
    # solution (do not include any coin)
    if (sum == 0):
        return 1

    # If sum is less than 0 then no
    # solution exists
    if (sum < 0):
        return 0

    # If there are no coins and sum
    # is greater than 0, then no
    # solution exist
    if (n <= 0):
        return 0

    # count is sum of solutions (i)
    # including coins[n-1] (ii) excluding coins[n-1]
    return count(coins, n - 1, sum) + count(coins, n, sum-coins[n-1])
#  A recursive solution for Rod cutting problem

#  Returns the best obtainable price for a rod of length n
#   and price[] as prices of different pieces 
def cutRod(price, index, n):
    
    #  base case
    if index == 0:
        return n*price[0]
      
      #v if n is 0 we cannot cut the rod anymore.
    if (n ==0):
        return 0
    
    #   At any index we have 2 options either
    #   cut the rod of this length or not cut 
    #   it
    notCut = cutRod(price,index - 1,n)
    cut = float("-inf")
    rod_length = index + 1

    if (rod_length <= n):
        
        cut = price[index]+cutRod(price,index,n - rod_length)
  
    return max(notCut, cut)

# A Naive recursive Python implementation of LCS problem


def lcs(X, Y, lx, ly):
    # if the lengths are 0 then there are no substrings
    if lx == 0 or ly == 0:
        return 0
    elif X[lx-1] == Y[ly-1]:
        return 1 + lcs(X, Y, lx-1, ly-1)
    else:
        return max(lcs(X, Y, lx, ly-1), lcs(X, Y, lx-1, ly))