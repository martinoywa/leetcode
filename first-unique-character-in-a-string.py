class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # generate dictionary of counts
        s_set = set(s)
        counts = {c: 0 for c in s_set}
        for c in s:
            counts[c] += 1

        # find first unique element
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        return -1
        
