func minCostClimbingStairs(cost []int) int {
    n := len(cost);
    if n == 0 {
        return 0;
    }
    if n == 1 {
        return cost[0];
    }
    if n == 2 {
        if cost[0] > cost[1] {
            return cost[1];
        }
        return cost[0];
    }

    i := 2;
    ret := 0;
    for {
        if i > n {
            break;
        }
        if cost[i - 1] > cost[i - 2] {
            ret = cost[i - 2];
        } else {
            ret = cost[i - 1]
        }

        if i == n {
            return ret;
        }
        cost[i] += ret;
        i += 1;
    }
    return ret;
}