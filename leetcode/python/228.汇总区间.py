class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []
        tmp = []
        for i in range(len(nums)):
            # print(i, nums[i], tmp, ret)
            if not tmp:
                tmp.append(str(nums[i]))
                continue
            if nums[i] - nums[i - 1] == 1:
                if len(tmp) > 1:
                    tmp[1] = str(nums[i])
                else:
                    tmp.append(str(nums[i]))
            else:
                ret.append(tmp)
                tmp = [str(nums[i])]
        if tmp:
            ret.append(tmp)
        res = []
        for tmp in ret:
            res.append('->'.join(tmp))
        return res