# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n

        while start < end:

            mid = start + int((end - start) / 2)
            if isBadVersion(mid):
                if mid == 1 or not isBadVersion(mid - 1):
                    return mid
                end = mid - 1
            else:
                start = mid + 1
        
        if start == end and isBadVersion(start):
            return start