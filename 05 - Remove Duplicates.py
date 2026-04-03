nums = [1,1,2]

def removeDuplicates( nums) -> int:
        duplicado = list(dict.fromkeys(nums))
        k: int = len(duplicado)
        return k



def removeDuplicates_2( nums) -> int:
    k = 1 
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]: 
            nums[k] = nums[i]      
            k += 1                 
    return k


def removeDuplicates_3( nums) -> int:
    k = 0
    for i in range (len(nums)):
        if (nums[k] != nums[i + 1]):
            nums[k] = nums[i]
            k += 1
    return k


    

def removeDuplicates_4( nums) -> int:
    k = 0
    for i in range ( len(nums)):
        if (i + 1 < len(nums) and nums[i] != nums[i + 1]):
            nums[k] = nums[i]
            k += 1
    return k

print(removeDuplicates_2(nums))