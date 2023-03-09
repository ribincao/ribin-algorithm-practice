func maxSubArray(nums []int) int {
    if len(nums) == 0 {
        return 0;
    };

    ret := nums[0];
    for i, _ := range nums {
        if i == 0 {
            continue;
        }
        if nums[i] + nums[i - 1] > nums[i] {
            nums[i] = nums[i] + nums[i - 1];
        }
        if nums[i] > ret {
            ret = nums[i];
        }
    }
    return ret;
}