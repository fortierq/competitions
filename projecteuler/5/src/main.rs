// smallest multiple

fn main() {
    
    let mut n = 1;
    loop {
        let mut found = true;
        for i in 2..21 {
            if n % i != 0 {
                found = false;
                break;
            }
        }
        if found {
            println!("n: {n}");
            break;
        }
        n += 1;
    }
}
