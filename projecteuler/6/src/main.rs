fn main() {
    let n = 100.;
    let s2:f32 = n*(n+1.)/2.;
    let s = s2.powf(2.) - (n*(n+1.)*(2.*n+1.)/6.) as f32;
    println!("{s}");
}
