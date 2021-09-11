for i in range(int(input())):
    a = int(input())
    i_last = -1
    last = "F"
    dp = [0]
    s = input()
    for j, c in enumerate(s):
        if c != "F" and s[i_last] != "F" and c != last:
            dp.append((dp[i_last + 1] + i_last + 1))
        else:
            dp.append(dp[-1])
        if c != "F":
            i_last = j
            last = c
    print(f"Case #{i+1}: {sum(dp) % 1_000_000_007}")
