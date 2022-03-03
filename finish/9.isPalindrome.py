class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        len_x = len(str_x)
        for i in range(0, len_x//2):
            if str_x[i] == str_x[len_x-1-i]:
                pass
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121251))
