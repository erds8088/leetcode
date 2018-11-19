class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        j = 0
        length = len(chars)
        for i in range(length):
            # 当遍历达到列表长度，或下一个元素不等于当前元素时，进行压缩
            if i+1 >= length or chars[i+1] != chars[i]:
                j += 1
                # 首先若计数不唯一，则记录计数至j处
                if count != 1:
                    for c in str(count):
                        chars[j] = c
                        j += 1
                # 当元素未达到边界时，还需把i+1处的元素提前到j处
                if i+1 < length:
                    chars[j] = chars[i+1]
                    # 重置计数
                    count = 1
            # i+1处位置的元素与i处的一致，则计数加1
            else:
                count += 1
        del chars[j:]
        return j
