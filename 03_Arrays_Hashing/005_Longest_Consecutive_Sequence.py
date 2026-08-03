# ---------------------------------------------------
# Problem: Longest Consecutive Sequence
# Category: Arrays & Hashing
# Difficulty: Medium
# Approach: Sorting (Brute Force)
# Time Complexity: O(n log n)
# Space Complexity: O(1) (using sort()) / O(n) if using sorted()
# ---------------------------------------------------

# Example 1 : 
nums = [5, 4, 6, 1, 3, 2] 
# Output = 4


def longest_consecutive_sequence(nums):

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

print(longest_consecutive_sequence(nums))