class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:

            sortedstr = "".join(sorted(string))

            if sortedstr not in hashmap:
                hashmap[sortedstr] = []
            hashmap[sortedstr].append(string)

        return list(hashmap.values())
