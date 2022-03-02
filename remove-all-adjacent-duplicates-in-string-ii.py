class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # create a stack
        stack = []
        # push elements and counts
        # if counts == k pop
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack and stack[-1][1] == k:
                stack.pop()
        # join with counts
        return "".join([_[0]*_[1] for _ in stack])
