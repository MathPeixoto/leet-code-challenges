import time


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        new_list = []

        for c in s:
            new_list.append(roman[c])

        total = 0
        for idx, val in enumerate(new_list):

            future_idx = (idx + 1)
            if future_idx <= len(new_list):

                if future_idx == len(new_list):
                    total += val

                elif val >= new_list[future_idx]:
                    total += val
                else:
                    total -= val

        return total


if __name__ == "__main__":
    begin = time.time()
    sol = Solution()
    end = time.time()
    print(sol.romanToInt("III"))
