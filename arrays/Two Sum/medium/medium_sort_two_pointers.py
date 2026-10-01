"""Sort, then move two pointers. Time: O(n log n). Extra space: O(n)."""


class Solution:
    def twoSum(self, nums, target):
        # Keep original indexes because sorting changes the positions.
        indexed_nums = sorted((number, index) for index, number in enumerate(nums))
        left = 0
        right = len(indexed_nums) - 1

        while left < right:
            total = indexed_nums[left][0] + indexed_nums[right][0]
            if total == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            if total < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
