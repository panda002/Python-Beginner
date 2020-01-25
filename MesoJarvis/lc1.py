nums = [3,2,4]
target = 6


def twoSum(nums, target):
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums:
            return nums.index(nums[i]), nums.index(diff)
        else:
            return False


print(twoSum(nums,target))