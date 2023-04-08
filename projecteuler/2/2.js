let [f0, f1, n] = [1, 2, 0]

while (f0 <= 4000000) {
    if (f0 % 2 == 0)
        n += f0
    const tmp = f0
    f0 = f1
    f1 += tmp
}

console.log(n)