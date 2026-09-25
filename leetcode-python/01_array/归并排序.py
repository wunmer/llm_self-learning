# mysort函数对传入的数组nums进行排序，输出排序后结果
def mymerge(left, right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else :
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def mysort(nums):
    if len(nums) < 2: return nums
    mid = len(nums)//2
    left = mysort(nums[:mid])
    right = mysort(nums[mid:])
    result = mymerge(left, right)
    return result

print(mysort([1,3,2,4,5]))
