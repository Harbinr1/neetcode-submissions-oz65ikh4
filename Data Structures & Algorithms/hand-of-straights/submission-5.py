class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freqNum = defaultdict(int)
        for n in hand:
            freqNum[n] += 1
        
        for card in sorted(freqNum.keys()):
            while freqNum[card] > 0:
                for i in range(groupSize):
                    next_card = card + i
                    if freqNum[next_card] == 0:
                        return False
                    else:
                        freqNum[next_card] -= 1
        return True
                    