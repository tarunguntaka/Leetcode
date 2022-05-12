def productExceptSelf(nums):

    l = len(nums)
    answer = [1 for i in range(l)]

    pre = 1 
    for i in range(l):
        answer[i] = answer[i]*pre 
        pre = pre*nums[i]

    post = 1
    for i in range(l-1,-1,-1):
        answer[i]= post*answer[i]
        post= post*nums[i]
    
    return answer

# def productExceptSelf(nums):
#         n = len(nums)
#         result = [1 for i in range(n)]
        
# #         adding prefix to output
#         pre = 1
#         for i in range(n):
#             result[i] *= pre
#             pre *= nums[i]
        
# #         adding postfix to output
#         post = 1
#         for i in range(n-1,-1,-1):
#             result[i] *= post
#             post *= nums[i]
        
#         return result

nums = [1,2,3,4]
print(productExceptSelf(nums))