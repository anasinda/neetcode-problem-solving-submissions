class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups_dict = {}
        for element in nums:
            dups_dict[element] = dups_dict.get(element, 0) + 1

        for value in dups_dict.values():
            if value > 1:
                return True
        return False