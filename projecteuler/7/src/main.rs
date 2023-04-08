fn main() {
    let n = 1000000;
    let mut prime = vec![true; n];
    let mut nprime = 0;
    for i in 2..n {
        if prime[i] {
            nprime += 1;
            if nprime == 10001 {
                println!("{i}");
            }
            let mut k = 2*i;
            while k < n {
                prime[k] = false;
                k += i;
            }
        }
    }
}
