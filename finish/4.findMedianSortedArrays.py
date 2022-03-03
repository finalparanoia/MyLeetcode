class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total_list = nums1 + nums2
        for i in range(0, len(total_list)):
            for num in range(1, len(total_list)):
                if total_list[num] < total_list[num-1]:
                    tmp = total_list[num-1]
                    total_list[num-1] = total_list[num]
                    total_list[num] = tmp

        len_list = len(total_list)
        if len_list % 2 == 1:
            return total_list[int(len_list / 2 - 0.5)]
        else:
            return (total_list[int(len_list / 2 - 1)] + total_list[int(len_list / 2)])/2