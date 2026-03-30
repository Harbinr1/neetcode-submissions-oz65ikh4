from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                count[index] += 1


            key = tuple(count)
            if key not in hashmap:
                hashmap[key] = [s]
            else:
                hashmap[key].append(s)

        return list(hashmap.values())