//Large sum
fn main() {
    let mut sum = 0;
    let mut s = String::new();
    loop {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        if s == "" {
            break;
        }
        sum += s[..10].parse::<u128>().unwrap();
    }
    println!("{}", sum);
}
