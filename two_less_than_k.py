def two_less_than_k(arr_unsorted: list[int], k: int) -> int:
    # First of all I need to order the list in ascendant order.
    arr_sorted = sorted(arr_unsorted)

    # Get the first index and the last index of the list
    left_index, right_index = 0, len(arr_sorted) - 1

    # I can initialize the max_sum with -1, that is the value that will be returned if there aren't elements in the
    # list that satisfies the required sum or will be returned the result of a sum less than K.
    max_sum = -1

    # Using binary search to while left_index is smaller thank right_index
    while left_index < right_index:

        # the sum in each iterate
        current_sum = arr_sorted[left_index] + arr_sorted[right_index]

        # check if the current sum is smaller or equal to K. If it is so that the max sum is updated
        # and the left_index is increased
        if current_sum <= k:
            max_sum = current_sum
            left_index += 1

        # if the current sum is greater than K the right_index needs to be decreased.
        elif current_sum > k:
            right_index -= 1

    return max_sum


if __name__ == '__main__':
    A = [34, 23, 1, 24, 75, 33, 54, 8]
    K = 60

    print(two_less_than_k(A, K))
