# ===================================================
# Problem: Top K Frequent Elements
# Category: Arrays & Hashing
# Difficulty: Medium
# ===================================================

# Problem Statement:
#
# Given an integer array nums and an integer k,
# return the k most frequent elements.
#
# You may return the answer in any order.
#

# Example:
#
# Input:
# nums = [1,1,1,2,2,3]
# k = 2
#
# Output:
# [1,2]
#
# Explanation:
# 1 appears 3 times.
# 2 appears 2 times.
# They are the two most frequent elements.
#

# ===================================================
# Approach 1: Sorting
# ===================================================
#
# Idea:
# 1. Count the frequency of each element using a dictionary.
# 2. Sort the dictionary items by frequency in descending order.
# 3. Take the first k elements.
# 4. Store the elements in a result list.
# 5. Return the result.
#
# Time Complexity: O(n + m log m)
#
# Space Complexity: O(m)
#
# m = Number of unique elements.
#
# ===================================================

def approach_1(nums, k):

    freq = {}

    # Count frequency
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Sort by frequency
    sorted_items = sorted(freq.items(),key=lambda x: x[1],reverse=True)

    result = []

    # Collect first k elements
    for key, value in sorted_items[:k]:
        result.append(key)

    return result



# ===================================================
# Approach 2: Bucket Sort
# ===================================================
#
# Idea:
# 1. Count the frequency of each element.
# 2. Create buckets where the bucket index represents
#    the frequency.
# 3. Place each number into its corresponding bucket.
# 4. Traverse buckets from highest frequency to lowest.
# 5. Return the first k elements collected.
#
# Time Complexity: O(n)
#
# Space Complexity: O(n)
#
# ===================================================

def approach_2(nums, k):

    # Step 1
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Step 2
    buckets = [[] for _ in range(len(nums) + 1)]

    # Step 3
    for num, count in freq.items():
        buckets[count].append(num)

    # Step 4
    result = []

    for i in range(len(buckets) - 1, 0, -1):

        for num in buckets[i]:

            result.append(num)

            if len(result) == k:
                return result




# ===================================================
# Test Cases
# ===================================================

# Test Case 1

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(approach_1(nums, k))
print(approach_2(nums, k))


# Test Case 2

nums = [1]
k = 1

print(approach_1(nums, k))
print(approach_2(nums, k))


# Test Case 3

nums = [4, 4, 4, 5, 5, 6]
k = 1

print(approach_1(nums, k))
print(approach_2(nums, k))


# ===================================================
# Interview Notes
# ===================================================
#
# ✔ Use a dictionary to count the frequency of each
#   element.
#
# ✔ Sorting is simple to implement and commonly
#   accepted in interviews.
#
# ✔ Bucket Sort removes the sorting step and achieves
#   O(n) time complexity.
#
# ✔ The bucket index represents the frequency of an
#   element.
#
# ✔ Maximum possible frequency is len(nums), so
#   len(nums) + 1 buckets are required.
#
# ✔ Multiple elements can have the same frequency,
#   therefore each bucket is a list.
#
# ✔ Traverse buckets from highest frequency to lowest
#   to retrieve the most frequent elements first.
#
# ✔ Return immediately after collecting k elements to
#   avoid unnecessary traversal.
#
# ✔ bucket[0] is always empty because no element can
#   appear zero times.
#

# ===================================================
# Approach Comparison
# ===================================================
#
# Approach              Time              Space
# ---------------------------------------------------------
# Sorting              O(n + m log m)     O(m)
# Bucket Sort          O(n)               O(n)
#
# Best Choice
#
# ✔ General interviews
#     → Sorting
#
# ✔ When O(n) optimization is requested
#     → Bucket Sort

