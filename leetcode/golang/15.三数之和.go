func threeSum(nums []int) [][]int {
    n, ret := len(nums), make([][]int, 0);
    if n == 0 {
        return ret;
    }
    sort.Ints(nums);
    for first := 0;first < n;first++ {
        if first > 0 && nums[first] == nums[first - 1] {
            continue
        };
        third := n - 1;
        target := 0 - nums[first];

        for second := first + 1;second < n;second++ {
            if second > first + 1 && nums[second] == nums[second - 1] {
                continue
            }
            for {
                if second >= third {
                    break
                }
                if nums[second] + nums[third] > target {
                    third -= 1;
                } else {
                    break;
                }
            }

            if second == third {
                break
            }

            if nums[second] + nums[third] == target {
                ret = append(ret, []int{nums[first], nums[second], nums[third]});
            }
        }
    }
    return ret;
}