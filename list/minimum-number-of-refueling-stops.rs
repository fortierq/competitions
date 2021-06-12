use std::collections::BinaryHeap;

impl Solution {
    pub fn min_refuel_stops(target: i32, mut fuel: i32, mut stations: Vec<Vec<i32>>) -> i32 {
        stations.push(vec![target, 0]);
        let mut heap : BinaryHeap<i32> = BinaryHeap::new(); // unused stations seen so far
        let mut k = 0; // number of refuels so far
        for s in stations.iter() {
            while fuel < s[0] {
                match heap.pop() {
                    Some(f) => {
                        fuel = fuel + f; 
                        k = k + 1
                    },
                    None => return -1
                }
            }
            heap.push(s[1]);
        }
        k
    }
}
