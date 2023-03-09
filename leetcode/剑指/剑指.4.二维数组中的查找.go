func findNumberIn2DArray(matrix [][]int, target int) bool {
    if len(matrix) == 0 {
        return false;
    }
    n, m := len(matrix), len(matrix[0]);
    row, col := 0, m - 1;
    for {
        if row >= n || col < 0 {
            break;
        }
        nums := matrix[row][col];
        if nums == target {
            return true;
        } else if nums < target {
            row += 1;
        } else {
            col -= 1;
        }
    }
    return false;
}