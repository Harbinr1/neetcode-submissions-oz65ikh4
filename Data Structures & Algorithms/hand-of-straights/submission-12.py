class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashMap = defaultdict(int)

        for val in hand:
            hashMap[val] += 1
        
        for card in sorted(hashMap.keys()):
            while hashMap[card] > 0 :
                for i in range(groupSize):
                    next_card = i + card
                    if hashMap[next_card] == 0:
                        return False
                    else:
                        hashMap[next_card] -= 1
        return True