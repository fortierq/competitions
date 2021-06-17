impl Solution {
    pub fn num_subarray_bounded_max(nums: Vec<i32>, left: i32, right: i32) -> i32 {
        let mut k = 0;
        let mut last_big = -1;
        let mut total = 0;
        for (i, &n) in nums.iter().enumerate() {
            if n > right {
                k = 0;
                last_big = i as i32;
            }
            else if n >= left {
                k = i as i32 - last_big;
            }
            total += k;
        }
        return total;
    }
}