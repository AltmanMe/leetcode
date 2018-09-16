class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_new = str.lstrip(' ')
        res = ''
        sign = False
        char_sign = ''
        output = 0
        if str_new == '' or str_new == '-' or str_new == '+':
            return 0
        for idx, char in enumerate(str_new):
            if char in ['-', '+'] and idx == 0:
                sign = True
                char_sign = char
            elif not char.isdigit() and idx == 0:
                return 0
            elif char.isdigit():
                res = res + char
            else: break
        if res == '':
            return 0
        if char_sign == '-':
            output = -int(res)
        else:
            output = int(res)
        output = self.check_range(output)
        return output

    def check_range(self, num):
        if num > pow(2,31)-1:
            return pow(2,31)-1
        elif num < -pow(2,31):
            return -pow(2,31)
        else:
            return num

"""
res maybe empty so line 23
and
we must make sure the sign we wanted to detect is the first char in str_new and
otherwise we may encounter error, for exapmle, when input is "+-2"
Worthly notice:
    def check_str(str):
        size = len(str)
        for idx, char in enumerate(str):
            if not char.isdigit():
                break
        if idx == size-1:
            return True, idx
        else:
            return False, idx
is not a good idea to find the whole effective number within whole string, for instance,
input: "40f" or "403"
"""
