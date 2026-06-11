class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        numset = set()
        output = []

        n = len(nums)
        for i in range(n):
            j = i +1
            k = n-1
            while(j < k):
                sum = nums[i] + nums[j]+nums[k]
                if sum == target:
                    numset.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif sum < target:
                    j+=1
                else:
                    k-=1
        
        for nums in numset:
            output.append(list(nums))
        
        return output
        