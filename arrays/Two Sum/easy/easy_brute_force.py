"""Try every pair. Time: O(n²)."""


class Solution:
    def twoSum(self, nums, target):
        for first in range(len(nums)):
            for second in range(first + 1, len(nums)):
                print("NUM", nums[first], nums[second])
                if nums[first] + nums[second] == target:
                    return [first, second]
        return []


if __name__ == "__main__":
    print(Solution().twoSum([3,2,4], 6))
