class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        final_list = []
        while i < len(strs):
            j = i + 1
            add_ele = []
            add_ele.append(strs[i])
            while j < len(strs):
                if sorted(strs[i]) == sorted(strs[j]):
                    element = strs.pop(j)
                    add_ele.append(element)
                else:
                    j += 1
            final_list.append(add_ele)
            i += 1
        if len(final_list) > 0:
            return final_list