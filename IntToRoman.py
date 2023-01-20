import time


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        romanized = ''

        for key, value in roman.items():
            num_key = (num // key)
            romanized += value * num_key
            num %= key

        else:
            return romanized


if __name__ == "__main__":
    begin = time.time()
    sol = Solution()
    end = time.time()
    print(sol.intToRoman(3))
