func findRepeatNumber(nums []int) int {
    Founded := make(map[int]bool);
    var ret int;
    for _, num := range nums {
        if _, ok := Founded[num];ok {
            ret = num;
            break;
        }
        Founded[num] = true;
    }
    return ret;
}