
fn main() {
    let mut v = [0; 1000];
    v[0] = 1;
    for i in 0..1000 {
        for j in 0..1000 {
            v[j] *= 2;
        }
        for j in 0..1000 {
            if v[j] > 9 {
                v[j + 1] += v[j] / 10;
                v[j] %= 10;
            }
        }
    }
    println!("{}", v.iter().sum::<u32>());
}
