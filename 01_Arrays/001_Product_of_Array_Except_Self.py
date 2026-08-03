# ===================================================
# Problem: Product of Array Except Self
# Category: Arrays / Prefix & Suffix Products
# Difficulty: Medium
# ===================================================

# Problem Statement:
#
# Given an integer array nums, return an array answer such that:
#
# answer[i] = product of all elements in nums except nums[i].
#
# Solve the problem without using division.
#

# Example:
#
# Input :
# nums = [1, 2, 3, 4]
#
# Output:
# [24, 12, 8, 6]
#
# Explanation:
#
# Index 0 -> 2 * 3 * 4 = 24
# Index 1 -> 1 * 3 * 4 = 12
# Index 2 -> 1 * 2 * 4 = 8
# Index 3 -> 1 * 2 * 3 = 6


# ===================================================
# Approach 1: Brute Force
# ===================================================
#
# Idea:
# 1. Traverse every element in the array.
# 2. For each index, calculate the product of all other elements.
# 3. Skip the current index while multiplying.
# 4. Store the product in the result array.
# 5. Return the result.
#
# Time Complexity : O(n²)
#
# Space Complexity: O(1) (excluding output array)
#
# ===================================================


def approach_1(nums):

    result = []

    for i in range(len(nums)):

        product = 1

        for j in range(len(nums)):

            if i != j:
                product *= nums[j]

        result.append(product)

    return result



# ===================================================
# Approach 2: Prefix & Suffix Products
# ===================================================
#
# Idea:
# 1. Create a prefix product array.
# 2. Create a suffix product array.
# 3. Prefix stores the product of all elements to the left.
# 4. Suffix stores the product of all elements to the right.
# 5. Multiply prefix and suffix values to get the answer.
#
# Time Complexity : O(n)
#
# Space Complexity: O(n)
#
# ===================================================





def approach_2(nums):

    left=[1]*len(nums)
    product = 1
    for i in range(1,len(nums)):
        product = product * nums[i-1]
        left[i]=product
    # print(left)

    right=[1]*len(nums)
    product = 1
    for i in range(len(nums)-2,-1,-1):
        product = product * nums[i+1]
        right[i]=product
    # print(right)

    result=[]
    for i in range(len(nums)):
        result.append(left[i]*right[i])

    return result


# ===================================================
# Approach 3: Optimized Prefix + Running Suffix Product
# ===================================================
#
# Idea:
# 1. Store prefix products directly in the result array.
# 2. Traverse from right to left.
# 3. Maintain a running suffix product.
# 4. Multiply the current result value with the suffix product.
# 5. Return the result.
#
# Time Complexity : O(n)
#
# Space Complexity: O(1) (excluding output array)
#
# ===================================================


def approach_3(nums):

    n = len(nums)

    result = [1] * n


    # Store prefix products
    product = 1

    for i in range(n):
        result[i] = product
        product *= nums[i]


    # Multiply by suffix products
    product = 1

    for i in range(n - 1, -1, -1):
        result[i] *= product
        product *= nums[i]


    return result



nums = [1,2,3,4]

print(approach_1(nums))
print(approach_2(nums))
print(approach_3(nums))

# ===================================================
# Test Cases
# ===================================================

# Test Case 1
#
# Input:
# nums = [1,2,3,4]
#
# Output:
# [24,12,8,6]


# Test Case 2
#
# Input:
# nums = [-1,1,0,-3,3]
#
# Output:
# [0,0,9,0,0]


# Test Case 3
#
# Input:
# nums = [5]
#
# Output:
# [1]


# ===================================================
# Interview Notes
# ===================================================
#
# ✔ Brute force solution is O(n²).
# ✔ Interviewers usually ask for an O(n) solution.
# ✔ Division is not allowed because of zero values.
# ✔ Prefix and suffix products eliminate repeated calculations.
# ✔ Optimized solution uses the output array to achieve O(1) extra space.

