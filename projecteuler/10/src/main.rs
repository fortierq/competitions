fn main() {
    let n = 2_000_000;
    let mut prime = vec![true; n];
    let mut s = 0;
    for i in 2..n {
        if prime[i] {
            s += i;
            for k in (2*i..n).step_by(i) {
                prime[k] = false;
            }
        }
    }
    println!("{s}")
}
