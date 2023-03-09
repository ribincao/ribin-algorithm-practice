var Fib map[int]int = map[int]int{0: 1, 1: 1}
func numWays(n int) int {
    if _, ok := Fib[n];ok {
        return Fib[n];
    }
    Fib[n] = (numWays(n - 1) + numWays(n - 2)) % 1000000007;
    return Fib[n];
}