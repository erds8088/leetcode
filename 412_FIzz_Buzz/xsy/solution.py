class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [str(i) if (i%3 and i%5) else "Fizz"*(i%3==0)+"Buzz"*(i%5==0) for i in range(1, n+1)]
