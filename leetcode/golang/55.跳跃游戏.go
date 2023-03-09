func canJump(nums []int) bool {
    n := len(nums);
    ret := make([]bool, n);
    ret[0] = true;

    i := 0;
    for {
        if i >= n || ret[i] == false {
            break
        }
        if nums[i] + i + 1 >= n {
            return true;
        }
        j := i + 1;
        for {
            if j >= nums[i] + i + 1 {
                break;
            }
            if nums[j] + j + 1 >= n {
                return true;
            }
            ret[j] = true;
            j += 1
        }
        i += 1;
    }
    return false;
}