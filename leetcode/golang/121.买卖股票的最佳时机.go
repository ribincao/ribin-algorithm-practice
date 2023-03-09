func maxProfit(prices []int) int {
    ret, i, j := 0, 0, 0;
    for {
        if j >= len(prices) - 1 {
            break;
        }
        profit := prices[j + 1] - prices[i];
        if profit > 0 {
            if profit > ret {
                ret = profit;
            }
        } else {
            i = j + 1;
        }
        j += 1;
    }
    return ret;
}