fn n_subarray(i: i32, j: i32) -> i32 {
    let sz = j - 1 - i;
    return sz*(sz + 1)/2;
}

impl Solution {
    pub fn num_subarray_bounded_max(nums: Vec<i32>, left: i32, right: i32) -> i32 {
        let mut k = 0;
        let mut last_big = -1;
        let mut valid = 0;
        let mut total = 0;
        for (i, &n) in nums.iter().enumerate() {
            if n > right {
                total += valid * n_subarray(last_big, i as i32);
                valid = 0;
                last_big = i as i32;
            }
            else if n >= left {
                valid = 1;
            }
        }
        return total + valid*n_subarray(last_big, nums.len() as i32);
    }
}