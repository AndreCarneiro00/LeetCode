from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_note_map = Counter(ransomNote)
        magazine_map = Counter(magazine)
        
        result = []
        for k, v in ransom_note_map.items():
            result.append(magazine_map.get(k) >= v)
        
        return all(result)