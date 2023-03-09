func generate(numRows int) [][]int {
    ret := make([][]int, numRows);
    i := 0;
    for i < numRows{
        tmp := make([]int, i + 1);
        j := 0;
        for j < len(tmp) {
            if j == 0 || j == len(tmp) - 1{
                tmp[j] = 1;
            } else {
                tmp[j] = ret[i - 1][j] + ret[i - 1][j - 1];
            }
            j += 1;
        }
        ret[i] = tmp;
        i += 1;
    }
    return ret
}