import time

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
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
    result = two_sum([3, 3], 6)
    end = time.time()
    print(result)
    print("Time: {}".format(end - begin))
