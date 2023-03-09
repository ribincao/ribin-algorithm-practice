func tribonacci(n int) int {
    var d []int = []int{0, 1, 1};
    if n < 3 {
        return d[n];
    }
    i := 3;
    for {
        if i == n + 1{
            break;
        }
        num := d[2] + d[1] + d[0];
        if i == n {
            return num;
        }
        d = append(d[1:], num);
        i += 1;
    }
    return d[n];
}