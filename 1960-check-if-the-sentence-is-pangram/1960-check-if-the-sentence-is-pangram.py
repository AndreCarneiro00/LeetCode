class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        n_available_letters = 26
        check = set()
        for letter in sentence:
            check.add(letter)
        
        return len(check) == 26