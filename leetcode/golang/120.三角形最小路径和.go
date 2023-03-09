func minimumTotal(triangle [][]int) int {
    if triangle == nil {
        return 0;
    }
    n := len(triangle);
    i := n - 2;
    for i >= 0 {
        j := 0;
        for j < i + 1 {
            a := triangle[i + 1][j];
            b := triangle[i + 1][j + 1];
            if a > b {
                triangle[i][j] += b;
            } else {
                triangle[i][j] += a;
            }
            j += 1;
        }
        i -= 1;
    }
    return triangle[0][0];
}