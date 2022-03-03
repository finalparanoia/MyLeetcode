class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if x < 0:
            flag = 1
            x = str(-x)
        else:
            x = str(x)
        result = ""
        for i in x:
            result = i + result
        if flag == 1:
            result = "-"+result
        result = int(result)
        if result not in range(-2**31, 2**31-1):
            result = 0
        return int(result)


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(-123))
