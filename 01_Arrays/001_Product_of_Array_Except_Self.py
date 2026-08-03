# Problem: Product of Array Except Self 
# Input nums = [1, 2, 3, 4] 
# Expected Output = [24, 12, 8, 6]

nums = [1, 2, 3, 4]

def Product_of_Array_Except_Self(nums):

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

print(Product_of_Array_Except_Self(nums))