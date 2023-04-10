// Problem 12

fn main() {
    let mut n = 1;
    let mut s = 0;
    let mut d = 0;
    while d < 500 {
        s += n;
        n += 1;
        d = 0;
        for i in 1..s {
            if s % i == 0 {
                d += 1;
            }
        }
    }
    println!("{s}")
}