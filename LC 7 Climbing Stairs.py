"""
      You are climbing a staircase. It takes n steps to reach the top.
      Each time you can either climb 1 or 2 steps.
      In how many distinct ways can you climb to the top?
      """

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        item1 = 1
        item2 = 2
        current = 0

        for i in range(n - 1):
            current = item1 + item2
            item1 = item2
            item2 = current

        return current

