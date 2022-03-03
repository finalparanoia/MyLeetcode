class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_str_len = 0
        for i in range(0, len(s)):
            tmp_s = s[i:]
            str_list = []
            for ii in tmp_s:
                if ii not in str_list:
                    str_list.append(ii)
                else:
                    break
            if len(str_list) > max_str_len:
                max_str_len = len(str_list)
        return max_str_len
