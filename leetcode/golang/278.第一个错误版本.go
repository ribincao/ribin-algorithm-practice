/** 
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad 
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

 func firstBadVersion(n int) int {
    start, end := 1, n;
    for {
        if start >= end {
            break;
        }
        mid := start + (end - start) / 2;
        if isBadVersion(mid) {
            if mid == 1 || !isBadVersion(mid - 1) {
                return mid;
            };
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    };
    if start == end && isBadVersion(start) {
        return start;
    }
    return start;
}