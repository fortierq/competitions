fn is_palindrome(n: u32) -> bool {
    let mut digits = Vec::new();
    let mut n = n;
    while n > 0 {
        digits.push(n % 10);
        n /= 10;
    }
    for i in 0..digits.len() / 2 {
        if digits[i] != digits[digits.len() - 1 - i] {
            return false;
        }
    }
    true
}

fn main() {
    let mut largest = 0;
    for i in 100..1000 {
        for j in 100..1000 {
            let product = i * j;
            if product > largest && is_palindrome(product) {
                largest = product;
            }
        }
    }
    println!("largest: {}", largest);
}
