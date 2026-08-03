# ===================================================
# Problem: Longest Consecutive Sequence
# Category: Arrays & Hashing
# Difficulty: Medium
# ===================================================

# Problem Statement:
# Given an unsorted array of integers nums,
# return the length of the longest consecutive
# elements sequence.
#
# The optimal solution should run in O(n).

# Example:
#
# Input :
# nums = [100,4,200,1,3,2]
#
# Output:
# 4
#
# Explanation:
# Longest consecutive sequence is
# 1 → 2 → 3 → 4

# ===================================================
# Approach 1: Sorting (Brute Force)
# ===================================================
#
# Idea:
# 1. Sort the array.
# 2. Traverse the sorted array.
# 3. Ignore duplicates.
# 4. Count consecutive numbers.
# 5. Track the maximum sequence length.
#
# Time Complexity : O(n log n)
#
# Space Complexity: O(1) using sort()
#                   O(n) using sorted()
#
# ===================================================

def longest_consecutive_sorting(nums):

    if nums:
        nums.sort()
        current=1
        longest=1
        for i in range(1,len(nums)):

            diff = nums[i]-nums[i-1]
            if diff==1:
                current+=1
            elif diff==0:
                continue
            else:
                current=1

            longest=max(longest,current)
    else:
        return 0
    
    return longest



# ===================================================
# Approach 2: Hash Set (Optimal)
# ===================================================
#
# Idea:
# 1. Convert the array into a Hash Set.
# 2. A number is the start only if (num-1)
#    is NOT present.
# 3. Start counting only from valid starts.
# 4. Extend the sequence using a while loop.
# 5. Track the maximum sequence length.
#
# Time Complexity : O(n)
#
# Space Complexity: O(n)
#
# ===================================================

def longest_consecutive_hashset(nums):

    if not nums:
        return 0

    nums_set = set(nums)
    longest = 1

    for num in nums_set:

        if num - 1 in nums_set:
            continue

        current_num = num
        length = 1

        while current_num + 1 in nums_set:
            current_num += 1
            length += 1

        longest = max(longest, length)

    return longest


# ===================================================
# Test Cases
# ===================================================

nums = [100,4,200,1,3,2]

print(longest_consecutive_sorting(nums.copy()))
print(longest_consecutive_hashset(nums))


# ===================================================
# Interview Notes
# ===================================================
#
# ✔ Sorting gives O(n log n).
# ✔ Hash Set lookup is O(1) average.
# ✔ Count only from sequence starts.
# ✔ Skip numbers whose predecessor exists.
# ✔ Use a while loop because the sequence length is unknown.













