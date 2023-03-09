func getRow(rowIndex int) []int {
    var d map[int][]int = map[int][]int{0: {1}, 1:{1, 1}};
    if _, ok := d[rowIndex];ok {
        return d[rowIndex];
    };

    tmp := getRow(rowIndex - 1);
    ret := make([]int, rowIndex + 1);
    i := 0;
    for i <= rowIndex {
        if i == 0 || i == rowIndex {
            ret[i] = 1;
        } else {
            ret[i] = tmp[i] + tmp[i - 1];
        }
        i += 1;
    }
    return ret;
}