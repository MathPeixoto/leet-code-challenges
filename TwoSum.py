import time

from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buffer_dictionary = {}
        for i, value in enumerate(nums):
            seeked_value = target - value

            if seeked_value in buffer_dictionary:
                # if a number shows up in the dictionary already
                # that means the necessary pair has been iterated on previously
                return [buffer_dictionary[seeked_value], i]

            # we insert the required number to pair with should it exist later in the list of numbers
            buffer_dictionary[value] = i


if __name__ == "__main__":
    begin = time.time()
    sol = Solution()
    end = time.time()
    print(sol.twoSum([3, 3], 6))
    print("Time: {}".format(end - begin))
