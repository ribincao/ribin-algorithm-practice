var Fib map[int]int = map[int]int{0: 0, 1: 1}
func fib(n int) int {
    if _, ok := Fib[n];ok {
        return Fib[n];
    }
    Fib[n] = (fib(n - 1) + fib(n - 2)) % 1000000007;
    return Fib[n];
}