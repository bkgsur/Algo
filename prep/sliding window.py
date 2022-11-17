def largestsubarray(A: [int]) -> (int, [int]):
    dp = [A[0]]

    [dp.append(max(dp[i - 1] + A[i], A[i])) for i in range(1, len(A))]
    return max(dp)


#print(largestsubarray([-2, 1, 6, 8, -20, 7]))
print(sum([11,14,9,16,10,20]))
