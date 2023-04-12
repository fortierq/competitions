use std::collections::HashMap;
fn aux(k: u128, h: &mut HashMap<u128, u128>) -> u128 {
    if !h.contains_key(&k) {
        let mut n = aux(if k % 2 == 0 { k / 2 } else { 3 * k + 1 }, h);
        h.insert(k, n + 1);
    }
    *h.get(&k).unwrap()
}

fn syr(n: u128) -> u128 {
    let mut h = HashMap::new();
    h.insert(1, 1);

    for i in 1..n {
        aux(i, &mut h);
    }
    *h.iter().max_by_key(|&(_, v)| v).unwrap().0
}

fn main() {
    println!("{}", syr(1_000_000));
}
