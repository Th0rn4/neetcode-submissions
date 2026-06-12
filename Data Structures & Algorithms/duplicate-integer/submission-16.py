class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        valueSeen = []

        for i in range(len(nums)):
            if nums[i] in valueSeen:
                return True
            else :
                valueSeen.append(nums[i])

        return False