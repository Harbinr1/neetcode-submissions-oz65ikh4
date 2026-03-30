from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = defaultdict(int)

        for char in s:
            hashmap[char] += 1
        
        for char in t:
            if hashmap[char] > 0:
                hashmap[char] -= 1
        
        for val in hashmap.values():
            if val != 0:
                return False
        return True
