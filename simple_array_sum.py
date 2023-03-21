import time


def simple_array_sum(nums: list[int]) -> int:
    total_sum = 0

    first_index, last_index = 0, len(nums) - 1

    while first_index <= last_index:

        first_value = nums[first_index]
        last_value = nums[last_index]

        #
        if first_index == last_index:
            partial_sum = first_value
            total_sum += partial_sum
            return total_sum

        if (first_index + 1) == last_index:
            partial_sum = first_value + last_value
            total_sum += partial_sum
            return total_sum
        else:
            partial_sum = first_value + last_value
            total_sum += partial_sum

            first_index += 1
            last_index -= 1


if __name__ == "__main__":
    begin = time.time()
    print(simple_array_sum([1, 2, 3, 4, 10, 11, 13]))
    end = time.time()
    print("Time: {}".format(end - begin))
