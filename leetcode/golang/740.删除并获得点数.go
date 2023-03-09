func deleteAndEarn(nums []int) int {
    max_val := 0;
    for _, num := range nums {
        if num > max_val {
            max_val = num;
        }
    }

    rob_nums := make([]int, max_val + 1);
    for _, item := range nums {
        rob_nums[item] += item;
    }

    ret := rob(rob_nums);
    return ret;
}

func rob(nums []int) int {
    i_2, i_1 := 0, 0;
    for _, num := range nums {
        tmp := i_1;
        if num + i_2 > i_1 {
            i_1 = num + i_2;
        }
        i_2 = tmp;
    }
    return i_1;
}