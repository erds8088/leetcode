class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if s == "(":
                stack.append(s)
            else:
                last = stack.pop()
                # 代表是"()"这种情况
                if last == "(":
                    stack.append(1)
                # 最后一个元素是数字
                else:
                    more_last = stack.pop()
                    # 若在这之前的一个元素是数字，则加起来，直到最后一个元素不是数字
                    while more_last != "(":
                        last += more_last
                        more_last = stack.pop()
                    stack.append(2*last)
        return sum(stack)


class Solution2:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        count = 0
        status = False
        ans = 0
        for s in S:
            if s == "(":
                count += 1
                status = True
            else:
                count -= 1
                if status:
                    ans += 2**(count*1)
                    status = False
        return ans
