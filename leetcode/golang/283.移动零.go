func moveZeroes(nums []int)  {
    n := len(nums);
    i, j := 0, 0;
    for {
        for {
            if i >= n || nums[i] == 0 {
                break;
            }
            i += 1;
        }

        for {
            if j >= n || nums[j] != 0 {
                break;
            }
            j += 1;
        }

        if i >= n || j >= n {
            break;
        }

        if i < j {
            tmp := nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
        j = i;
    }
}