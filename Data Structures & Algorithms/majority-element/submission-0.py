class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        
        for j, count in counts.items():
            if count > len(nums)//2:
                return j