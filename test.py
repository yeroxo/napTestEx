class Solution:
    dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    @classmethod
    def romanToInt(cls, s: str) -> int:
        sum = 0
        prev = 0
        prev_count = 0
        for digit in s[::-1]:
            current = Solution.dict[digit]
            if prev > current:
                if (current in (100, 10, 1)) and prev_count != 1:
                    sum -= Solution.dict[digit]
                    prev_count += 1
                else:
                    raise ValueError("BadSubtractionDigit")
            else:
                prev_count = 0
                prev = Solution.dict[digit]
                sum += Solution.dict[digit]
        return sum


if __name__ == '__main__':
    while True:
        try:
            print(Solution.romanToInt(input()))
        except ValueError:
            print("Wrong number, Try again")
            pass
