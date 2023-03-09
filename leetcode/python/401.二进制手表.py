class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0: return ['0:00']
        nums = ['1'] * turnedOn + (10 - turnedOn) * ['0']
        times = []

        def dfs(x):
            if x == 10:
                s = ''.join(nums)
                if s not in times:
                    times.append(s)
                    return
            for i in range(x, 10):
                if x != i and nums[i] == nums[x]:
                    continue
                nums[x], nums[i] = nums[i], nums[x]
                dfs(x + 1)
                nums[x], nums[i] = nums[i], nums[x]

        dfs(0)
        ret = []
        for time in times:
            hour, minute = int(time[:4], 2), int(time[4:], 2)
            check_hour, check_minute = False, False
            if 0 <= hour <= 11:
                check_hour = True
            if 0 <= minute <= 59:
                check_minute = True
            if check_hour and check_minute:
                h, m = str(hour), str(minute)
                if minute < 10:
                    m = '0' + m
                t = h + ':' + m
                ret.append(t)

        return ret