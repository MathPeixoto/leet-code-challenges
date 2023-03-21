def missing_numbers(nums: list[int]) -> list[int]:
    buffer_array = []

    for value in nums:
        if value not in buffer_array:
            buffer_array.append(value)
        else:
            last_element = nums[-1]
            nums.remove(value)
            nums.append(last_element + 1)

    return nums


if __name__ == '__main__':
    A = [1, 2, 2, 3, 4]

    print(missing_numbers(A))
