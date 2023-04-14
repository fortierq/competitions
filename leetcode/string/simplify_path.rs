impl Solution {
    pub fn simplify_path(path: String) -> String {
        format!(
            "/{}",
            path.split('/')
                .filter(|&x| x != "" && x != ".")
                .fold(vec![], |mut acc, item| {
                    if item == ".." {
                        acc.pop();
                    } else {
                        acc.push(item);
                    }
                    acc
                })
                .join("/")
        )
    }
}
