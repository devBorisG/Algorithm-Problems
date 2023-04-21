class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Way to without convert int to str
        aux = x
        numero = 0
        while aux > 0:
            numero = 10*numero+aux%10
            aux //= 10
        return x == numero
        # Way to convert int to str (optimal)
        # return str(x)==str(x)[::-1]