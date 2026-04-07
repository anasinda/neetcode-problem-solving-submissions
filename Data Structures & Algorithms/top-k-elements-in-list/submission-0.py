class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        no_dups = list(set(nums))
        if len(no_dups) > 0 and k <= len(no_dups):
            final_list = []
            hash_map = dict()
            for num in nums:
                hash_map[num] = hash_map.get(num, 0) + 1

            for num in range(k):
                max_num = max(hash_map, key=hash_map.get)
                final_list.append(max_num)
                del hash_map[max_num]
            return final_list
