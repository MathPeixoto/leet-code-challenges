def twoLessThankK(A: list[int], K: int) -> int:
    # First of all I need to order the list in ascendant order.
    B = sorted(A)

    # Get the first index and the last index of the list
    left_index, right_index = 0, len(B) - 1

    # I can initialize the max_sum with -1, that is the value that will be returned if there aren't elements in the
    # list that satisfies the required sum or will be returned the result of a sum less than K.
    max_sum = -1

    # Using binary search to while left_index is smaller thank right_index
    while left_index < right_index:

        # the sum in each iterate
        current_sum = B[left_index] + B[right_index]

        # check if the current sum is smaller or equal to K. If it is so that the max sum is updated
        # and the left_index is increased
        if current_sum <= K:
            max_sum = current_sum
            left_index += 1

        # if the current sum is greater than K the right_index needs to be decreased.
        elif current_sum > K:
            right_index -= 1

    return max_sum


if __name__ == '__main__':
    A = [34, 23, 1, 24, 75, 33, 54, 8]
    K = 60

    print(twoLessThankK(A, K))
