func isPowerOfTwo(n int) bool {
    ret := 0;
    for n != 0 {
        if ret > 1 {
            return false;
        }
        if n & 1 == 1 {
            ret += 1;
        }
        n >>= 1;
    }
    return ret == 1;
}