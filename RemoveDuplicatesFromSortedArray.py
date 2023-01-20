import time
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        buffer_array = []

        for value in nums[::-1]:
            if value in buffer_array:
                nums.remove(value)
            else:
                buffer_array.append(value)

        return len(nums)


if __name__ == "__main__":
    begin = time.time()
    sol = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    size = sol.removeDuplicates(nums)
    end = time.time()

    print("Size: {}".format(size))
    print("Without Duplications: {}".format(nums))
    print("Time: {}".format(end - begin))
