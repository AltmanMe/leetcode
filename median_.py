"""
The overall run time complexity should be O(log(m+n))

python2 version
def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0
explanation: https://leetcode.com/problems/median-of-two-sorted-arrays/solution/
"""

def findMedianSortedArrays(nums1, nums):
    if nums1 or nums2:
        nums = sorted(list(nums1) + list(nums2))
        length = len(nums)
        if(length%2==0):
            return (nums[int(length/2 -1)]+nums[int(length/2)])/2
        else:
            return nums[int((length+1)/2)-1]
    else:
        return 0

"""
Timsort algorithm for built-in sorted function
Best case O(n)
Average case O(nlogn)
Worst case O(nlogn)
"""
