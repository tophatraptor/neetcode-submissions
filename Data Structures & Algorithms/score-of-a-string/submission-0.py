class Solution:
    def scoreOfString(self, s: str) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        atoi = {}
        for i, x in enumerate(alphabet):
            atoi[x] = i
        total = 0
        for i in range(len(s) - 1):
            if atoi[s[i]] - atoi[s[i+1]] < 0:
                total += atoi[s[i+1]] - atoi[s[i]]
            else:
                total += atoi[s[i]] - atoi[s[i+1]]
        return total