class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        anwser = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    anwser.append(i) 
                    anwser.append(j)
        if len(anwser) > 0:
            return anwser
        return None
