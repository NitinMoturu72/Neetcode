from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_Map = defaultdict(list)

        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c)-ord("a")] += 1
            
            key = tuple(count)
            anagram_Map[key].append(i)

        return list(anagram_Map.values())
