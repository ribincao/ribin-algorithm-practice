func twoSum(numbers []int, target int) []int {
    n := len(numbers);
    i, j := 0, n - 1;
    ret := make([]int, 2)
    for {
        if i >= j {
            break;
        }
        num := numbers[i] + numbers[j];
        if num == target {
            ret[0] = i + 1;
            ret[1] = j + 1;
            break;
        } else if num < target {
            i += 1;
        } else {
            j -= 1;
        }
    }
    return ret;
}