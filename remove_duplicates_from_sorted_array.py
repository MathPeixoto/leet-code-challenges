import time
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    buffer_array = []

    for value in nums[::-1]:
        if value in buffer_array:
            nums.remove(value)
        else:
            buffer_array.append(value)

    return len(nums)


if __name__ == "__main__":
    begin = time.time()
    nums_arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    size = remove_duplicates(nums_arr)
    end = time.time()

    print("Size: {}".format(size))
    print("Without Duplications: {}".format(nums_arr))
    print("Time: {}".format(end - begin))
