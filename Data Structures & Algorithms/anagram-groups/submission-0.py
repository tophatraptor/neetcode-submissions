class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for x in strs:
            sorted_str = ''.join(sorted(x))
            if sorted_str not in anagrams_dict:
                anagrams_dict[sorted_str] = [x]
            else:
                anagrams_dict[sorted_str].append(x)
        results = []
        for x in anagrams_dict:
            results.append(anagrams_dict[x])
        return results