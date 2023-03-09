func searchInsert(nums []int, target int) int {
    start, end := 0, len(nums) - 1;

    for {
        if start >= end {
            break;
        }
        mid := start + (end - start) / 2;
        if nums[mid] == target {
            return mid;
        } else if nums[mid] > target {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    if nums[start] >= target {
        return start;
    }
    return start + 1;
}