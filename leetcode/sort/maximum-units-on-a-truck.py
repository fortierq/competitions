impl Solution {
    pub fn maximum_units(mut box_types: Vec<Vec<i32>>, mut truck_size: i32) -> i32 {
        box_types.sort_by(|a, b| b[1].cmp(&a[1]));
        let mut n = 0;
        for b in box_types.iter() {
            let p = if truck_size > b[0] {b[0]} else {truck_size};
            n += p*b[1];
            truck_size -= p;
        }
        n
    }
}
