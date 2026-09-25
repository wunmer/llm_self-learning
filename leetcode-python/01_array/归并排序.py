# # mysort函数对传入的数组nums进行排序，输出排序后结果
# def mymerge(left, right):
#     i = j = 0
#     res = []
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             res.append(left[i])
#             i += 1
#         else :
#             res.append(right[j])
#             j += 1
#     res.extend(left[i:])
#     res.extend(right[j:])
#     return res

# def mysort(nums):
#     if len(nums) < 2: return nums
#     mid = len(nums)//2
#     left = mysort(nums[:mid])
#     right = mysort(nums[mid:])
#     result = mymerge(left, right)
#     return result

# print(mysort([1,3,2,4,5]))




def merge(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i]<= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def sort(nums):
    if len(nums)<= 1:return nums
    mid = len(nums)//2
    left = sort(nums[:mid])
    right = sort(nums[mid:])
    return merge(left,right)

print(sort([1,3,2,4,5]))