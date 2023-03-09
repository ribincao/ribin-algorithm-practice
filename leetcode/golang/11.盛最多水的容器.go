func maxArea(height []int) int {
    n := len(height)
    if n < 2 {
        return 0;
    }

    ret := 0;
    tmp := 0;
    i, j := 0, n - 1;
    for i < j {
        if height[i] < height[j] {
            tmp = height[i] * (j - i);
            i += 1;
        } else {
            tmp = height[j] * (j - i);
            j -= 1;
        }

        if tmp > ret {
            ret = tmp;
        }
    }
    return ret;
}