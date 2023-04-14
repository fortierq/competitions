struct Solution {

}

impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut s = Vec::new();
        let mut j = 0;
        for &e in &pushed {
            s.push(e);
            while !s.is_empty() && j < popped.len() && *s.last().unwrap() == popped[j] {
                s.pop();
                j += 1
            }
        }
        s.is_empty()
    }
}

fn main() {
    let (pushed, popped) = (vec![1,2,3,4,5], vec![4,3,5,1,2]);
    println!("{}", Solution::validate_stack_sequences(pushed, popped));
}