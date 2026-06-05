class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = count.get(num,0)+1


        sortarray = []
        for key,value in count.items():
            sortarray.append([value,key])

        sortarray.sort()

        answer = []
        i = 0
        while i != k:
            answer.append(sortarray.pop()[1])
            i+=1
        
        return answer

        