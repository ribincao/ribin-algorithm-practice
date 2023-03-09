func rotate(nums []int, k int)  {
    k = k % len(nums);
    swap(&nums, 0, len(nums) - 1);
    swap(&nums, 0, k - 1);
    swap(&nums, k, len(nums) - 1);
}

func swap(nums *[]int, start int, end int) {
    for {
        if start >= end {
            break
        }
        tmp := (*nums)[start];
        (*nums)[start] = (*nums)[end];
        (*nums)[end] = tmp;
        start += 1;
        end -= 1;
    }
}