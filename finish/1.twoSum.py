class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        pop_num = 0
        while True:
            pop_num = pop_num + 1
            tmp = target - nums.pop(0)
            if tmp in nums:
                return [pop_num-1, pop_num + nums.index(tmp)]
