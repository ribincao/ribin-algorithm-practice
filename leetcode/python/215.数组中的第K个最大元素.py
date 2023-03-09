class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ret = heapq.nlargest(k, nums)

        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, num)
        # ret = heapq.nlargest(k, heap)
        return ret[-1]