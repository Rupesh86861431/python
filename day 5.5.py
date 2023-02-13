def findPeak(nums, left=None, right=None):
    if left is None and right is None:
        left, right = 0, len(nums) - 1
    mid = (left + right) // 2
    if ((mid == 0 or nums[mid - 1] <= nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] <= nums[mid])):
        return mid
    if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
        return findPeak(nums, left, mid - 1)
    return findPeak(nums, mid + 1, right)
def findPeakElement(nums) -> int:
    if not nums:
        exit(-1)
    index = findPeak(nums)
    return nums[index]
if __name__ == '__main__':
    nums = [1,2,3,1]
    print('The peak element is', findPeakElement(nums))
