class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxcount = 0

        for num in numset:
            if num-1 not in numset:
                currentnum = num
                count = 1
                while (currentnum + 1) in numset:
                    currentnum +=1
                    count+=1
                maxcount = max(maxcount,count)
        return maxcount
                
        