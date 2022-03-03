class Solution:
    def myAtoi(self, s: str) -> int:
        new = ""
        for i in s:
            if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "+", "."]:
                new = new + i
        try:
            int_new = int(new)
            if int_new < -2**31:
                return -2**31
            elif int_new > 2**31 - 1:
                return 2**31 - 1
            else:
                return int_new
        except:
            return 0
