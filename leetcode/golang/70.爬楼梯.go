var d map[int]int = map[int]int{1: 1, 2: 2};
func climbStairs(n int) int {
    if _, ok := d[n];ok {
        return d[n];
    }
    d[n] = climbStairs(n - 1) + climbStairs(n - 2);
    return d[n];
}