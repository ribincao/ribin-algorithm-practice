func canWinNim(n int) bool {
    ret := n % 4;
    return !(ret == 0);
}