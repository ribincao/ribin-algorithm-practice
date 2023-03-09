func matrixReshape(mat [][]int, r int, c int) [][]int {
    n := len(mat);
    if n == 0 {
        return mat;
    }
    m := len(mat[0]);
    if m == 0 {
        return mat;
    }
    if m * n != r * c {
        return mat;
    }
    
    rr := 0;
    ret := make([][]int, r)
    for {
        if rr >= r {
            break;
        }
        rows := make([]int, c);
        ret[rr] = rows;
        rr += 1;
    }

    i := 0;
    for {
        if i >= n {
            break;
        }
        j := 0;
        for {
            if j >= m {
                break;
            }
            idx := i * m + j;

            row := idx / c;
            col := idx % c;
            ret[row][col] = mat[i][j]

            j += 1;
        }
        i += 1;
    }
    return ret;
}