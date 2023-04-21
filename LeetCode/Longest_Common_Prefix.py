class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        strs = sorted(strs)
        frst = strs[0]
        lst = strs[-1]
        for letter in range(min(len(frst),len(lst))):
            if frst[letter] != lst[letter]:
                return result
            else:
                result+=frst[letter]
        return result