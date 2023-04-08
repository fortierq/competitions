let n = parseInt(Math.sqrt(600851475143))
let p = Array(n).fill(true)
let largest = 2

for (let i = 2; i < n; i++) {
    if (p[i]) {
        for (let j = i * 2; j <= n; j += i) {
            p[j] = false
        }
        if (600851475143 % i === 0) {
            largest = i
        }
    }
}
console.log(largest)
