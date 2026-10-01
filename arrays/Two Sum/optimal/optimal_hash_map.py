"""Remember earlier numbers. Expected time: O(n). Extra space: O(n)."""


class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [seen[complement], index]
            # Check before storing so we cannot reuse the current index.
            seen[number] = index
        return []


if __name__ == "__main__":
    print(Solution().twoSum([3,2,4], 6))
