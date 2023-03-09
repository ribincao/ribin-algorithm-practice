func productExceptSelf(nums []int) []int {
    n := len(nums);
    if n == 1{
        return nums;
    }
    ret := make([]int, n);
    ret[0] = 1;
    for i, _ := range ret {
        if i == 0 {
            continue;
        }
        ret[i] = ret[i - 1] * nums[i - 1];
    }
    j := n - 2;
    t := 1;
    for j >= 0 {
        t *= nums[j + 1]
        ret[j] *= t;
        j -= 1;
    }
    return ret;
}