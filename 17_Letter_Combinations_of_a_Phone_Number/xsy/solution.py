class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {
            "1": "",     "2": "abc", "3": "def", 
            "4": "ghi",  "5": "jkl", "6": "mno", 
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = [""] if digits else []
        for digit in digits:
            lst = phone[digit]
            new = []
            for char in lst:
                for s in result:
                    new.append(s+char)
            result = new
        return result
