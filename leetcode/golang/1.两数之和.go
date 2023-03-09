func twoSum(nums []int, target int) []int {
    d, ret := make(map[int]int), make([]int, 2);
    for i, num := range nums {
        if _, ok := d[target - num];!ok {
            d[num] = i;
        } else {
            ret[0] = d[target - num];
            ret[1] = i;
            return ret;
        }
    }
    return ret;
}