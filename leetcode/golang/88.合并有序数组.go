func merge(nums1 []int, m int, nums2 []int, n int)  {
    i, j := m - 1, n - 1;

    for {
        if i < 0 || j < 0 {
            break;
        }
        if nums1[i] >= nums2[j] {
            nums1[i + j + 1] = nums1[i];
            i -= 1;
        } else {
            nums1[i + j + 1] = nums2[j];
            j -= 1;
        }
    }
    for {
        if j < 0 {
            break;
        }
        nums1[j] = nums2[j];
        j -= 1;
    }
}