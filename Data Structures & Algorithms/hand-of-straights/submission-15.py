class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freqCard = defaultdict(int)
        for card in hand:
            freqCard[card]+= 1
        
        for card in sorted(freqCard.keys()):
            while freqCard[card] > 0:
                for i in range(groupSize):
                    next_card = i + card
                    if freqCard[next_card] == 0:
                        return False
                    else:
                        freqCard[next_card] -= 1
        return True
        