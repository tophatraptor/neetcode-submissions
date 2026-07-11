class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        ct = Counter(hand)
        while len(ct) > 0:
            i = min(ct)
            for k in range(i, i + groupSize):
                if k in ct:
                    ct[k] -= 1
                    if ct[k] == 0:
                        ct.pop(k)
                else:
                    return False
        return True