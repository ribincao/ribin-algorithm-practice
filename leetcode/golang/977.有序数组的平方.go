func sortedSquares(nums []int) []int {
    i, j := 0, len(nums) - 1;
    k := j;
    ret := make([]int, j + 1);

    for {
        if i == j {
            ret[k] = nums[i] * nums[i];
            break;
        }
        a, b := nums[i] * nums[i], nums[j] * nums[j];
        if a < b {
            ret[k] = b;
            j -= 1;
        } else {
            ret[k] = a;
            i += 1;
        }
        k -= 1;
    }
    return ret;
}