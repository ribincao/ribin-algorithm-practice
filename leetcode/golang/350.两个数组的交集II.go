func intersect(nums1 []int, nums2 []int) []int {
    d := make(map[int]int);
    ret := make([]int, 0);

    for _, item := range nums1 {
        if _, ok := d[item];!ok {
            d[item] = 0;
        }
        d[item] += 1;
    }

    for _, num := range nums2 {
        if _, ok := d[num];ok {
            if d[num] > 0 {
                ret = append(ret, num);
                d[num] -= 1;
            }
        }
    }
    return ret;
}