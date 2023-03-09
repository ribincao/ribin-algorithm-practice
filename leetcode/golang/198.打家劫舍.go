func rob(nums []int) int {
    i_1, i_2 := 0, 0;
    for _, num := range nums {
        if num + i_2 > i_1 {
            tmp := num + i_2;
            i_2 = i_1;
            i_1 = tmp;
        } else {
            i_2 = i_1;
        }
    }
    return i_1;
}