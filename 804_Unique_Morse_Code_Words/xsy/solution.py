class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        codes = set()
        for word in words:
            # 'a' is 97
            temp = map(lambda i: morse[ord(i)-97], word)
            codes.add("".join(temp))
        return len(codes)
