func jump(nums []int) int {
    goal := len(nums) - 1;
    ret := 0;
    for goal > 0 {
        for i, num := range nums {
            if num + i >= goal {
                goal = i;
                ret += 1;
                break;
            }
        }
    }
    return ret;
}