// https://leetcode.com/problems/implement-strstr/

fn subword(m: &str, text: &str) -> i32 {
    let n = m.len();
    let p = text.len();
    if n > p {
        return -1;
    }
    for i in 0..(p - n + 1) {
        if m == &text[i..(i+n)] {
            return i as i32;
        }
    }
    return -1;
}

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        subword(&needle, &haystack)
    }
}