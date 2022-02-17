class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # string
        s = ""
        # counts
        counts = 0
        # current char
        char = chars[0]
        
        # get counts
        for c in chars:
            if char == c:
                counts += 1
            else:
                if counts == 1:
                    s += str(char)
                else:
                    s += str(char)
                    s += str(counts)
                char = c
                counts = 1
        if counts == 1:
            s += str(char)
        else:
            s += str(char)
            s += str(counts)
        chars[:] = [i for i in s]
        print(chars)
