class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        # for k == 0
        if k == 0:
            counts = {i: 0 for i in nums}
            for i in nums:
                counts[i] += 1
            # print(counts)
            fin = 0
            for v in counts.values():
                if v > 1:
                    fin += 1
            return fin
            
        # list of unique pairs
        unique = set()
        # itertate
        for i in range(len(nums)):
            # for j in range(i+1, len(nums)):
            #     if abs(nums[i] - nums[j]) == k:
            #         # print(nums[i], nums[j], i, j)
            #         # sort the pair
            #         pair = tuple(sorted((nums[i], nums[j])))
            #         unique.add(pair)
            if nums[i] + k <= max(nums) and nums[i] + k in nums:
#                 print(sorted([nums[i], nums[i] + k]))
                unique.add(tuple(sorted([nums[i], nums[i] + k])))
        
#         print(unique)
#         print()
        return len(unique)
