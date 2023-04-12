impl Solution {
    pub fn remove_stars(s: String) -> String {
        let s2 = String::from("");
        for c in &s {
            match c {
                '*' => {s2.pop();}
                c => {s2.push(c);}
            }
        }
        s2
    }
}