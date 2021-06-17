impl Solution {
    pub fn num_subarray_bounded_max(nums: Vec<i32>, left: i32, right: i32) -> i32 {
        let (mut i, mut j) = (-1, -1);
        let mut total = 0;
        for (k, &n) in nums.iter().enumerate() {
            if n > right {
                i = k as i32;      
            }
            if n >= left {
                j = k as i32;
            }
            total += (j - i);
        }
        return total;
    }
}