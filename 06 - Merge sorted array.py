nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
def merge( nums1, m , nums2, n) -> None:
    newArray = []
    for i in range(m):
        newArray.append(nums1[i])
    for j in range(n):
        newArray.append(nums2[j])
    newArray.sort()
    nums1 = newArray
    return nums1



def merge_2( nums1, m , nums2, n) -> None:
    k = 0
    for i in range(m):
        nums1[k] = nums1[i]
        k += 1
    for j in range(n):
        nums1[k] = nums2[j]
        k += 1
    nums1.sort()
    return nums1

print(merge_2(nums1, m , nums2, n))