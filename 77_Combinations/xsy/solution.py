class Solution:
    def combine(self, n, k):
        """
        求1...n数中k个数的组合, 可归纳为以下两步:
            1. 求1...n-1数中k个数的组合
            2. 求1...n-1数中k-1个数的组合（每种组合额外添加n）
            其中，n-1 >= k
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []
        if n == k:
            return [i for i in range(1, n+1)]
        if n > k:
            return self.combine(n-1, k)