impl Solution {
    pub fn is_valid(s: String) -> bool {
        let pile = Vec::new();
        for c in pile.chars() {
            match c {
                '(' => pile.push(')'),
                '[' => pile.push(']'),
                '{' => pile.push('}'),
                _ => {
                    if pile.is_empty() || pile.pop() != Some(c) {
                        return false;
                    }
                }
            }
        }
    }
}