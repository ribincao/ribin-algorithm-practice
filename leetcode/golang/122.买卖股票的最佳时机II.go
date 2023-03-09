func maxProfit(prices []int) int {
    buy := prices[0];
    ret := 0;
    for _, sell := range prices {
        if sell > buy {
            ret += (sell - buy);
        }
        buy = sell;
    }
    return ret;
}