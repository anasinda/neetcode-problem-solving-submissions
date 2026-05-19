class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result_list = []
        lenght = len(nums)
        index = 0
        while index < lenght:
            res = 1
            popped = nums.pop(0)
            for num in nums:
                res *= num
            result_list.append(res)
            nums.append(popped)
            index += 1
        return result_list
