func containsDuplicate(nums []int) bool {
    Store := make(map[int]bool);
    for _, num := range nums {
        if _, ok := Store[num];ok {
            return true;
        }
        Store[num] = true;
    }
    return false;
}