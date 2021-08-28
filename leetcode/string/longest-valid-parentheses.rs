use std::cmp::max;

impl Solution {
    pub fn longest_valid_parentheses(s: String) -> i32 {
        let mut stack = Vec::new();
        stack.push(-1);
        let mut n = 0;
        for (i, c) in s.chars().enumerate() {
            match c {
                '(' => stack.push(i as i32),
                _ => {
                    stack.pop();
                    match stack.last() {
                        None => stack.push(i as i32),
                        Some(j) => n = max(n, i as i32 - j),
                    }
                }
            }
        }
        n
    }
}
