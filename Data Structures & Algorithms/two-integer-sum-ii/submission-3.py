class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for index, i_num in enumerate(numbers):
            for jndex, j_num in enumerate(numbers[1:], 1):
                if i_num + j_num == target:
                    return [index + 1, jndex + 1]
