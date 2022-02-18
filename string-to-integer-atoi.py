class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge cases
        if len(s) == 0:
            return 0
        elif (len(s) == 1 and s == "-") or (len(s) == 1 and s == "+"):
            return 0
        # number
        number = ""
        # white spaces
        s = s.lstrip()
        if len(s) == 0:
            return 0
        # check for sign
        if s[0] == "-": 
            number += "-"
            s = s[1:]
        elif s[0] == "+":
            number += "+"
            s = s[1:]
        # iterate over s
        for c in s:
            try:
                if int(c) or int(c) == 0:
                    number += c
            except:
                if number and number == "-":
                    return 0
                elif number and number == "+":
                    return 0
                elif number:
                    break
                else:
                    return 0
            
        if -2**31 <= int(number) <= 2**31-1:
            return int(number)
        elif int(number) < -2**31:
            return -2**31
        else:
            return 2**31-1
            
