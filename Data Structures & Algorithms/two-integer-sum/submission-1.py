class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        answer = []
        for i in range (len(nums)):
            difference = target-nums[i]
            if difference in hashmap:
                answer.append(hashmap[difference])
                answer.append(i)
                return answer
            hashmap[nums[i]] = i
