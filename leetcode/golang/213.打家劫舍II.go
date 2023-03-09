func rob(nums []int) int {
    n := len(nums);
    if n == 1 {
        return nums[0];
    }
    left := rob2(nums[:n - 1]);
    right := rob2(nums[1:]);
    if left > right {
        return left;
    }
    return right;
}

func rob2(nums []int) int {
    i_1, i_2 := 0, 0;
    for _, num := range nums {
        tmp := i_1;
        if num + i_2 > i_1 {
            i_1 = num + i_2;
        }
        i_2 = tmp;
    }
    return i_1;
}