class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operations = {
            "+": "ADD",
            "-": "SUB",
            "*": "MUL",
            "/": "DIV",
        }
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                operation = operations[token]
                number2, number1 = stack.pop(), stack.pop()
                if operation == "ADD":
                    number = number1 + number2
                elif operation == "SUB":
                    number = number1 - number2
                elif operation == "MUL":
                    number = number1 * number2
                else:
                    number = int(number1 / number2)
                stack.append(number)
        return stack.pop()


s = Solution()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
