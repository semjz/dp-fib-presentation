import time

memo = [0, 1]


def fib(n):
    for i in range(2, n + 1):
        memo.append(memo[i - 1] + memo[i - 2])
    return memo[n]


n = int(input())
start_time = time.perf_counter()
result = fib(n)
end_time = time.perf_counter()
time_elapsed = end_time - start_time
print(f"result:{result}, time elapsed: {time_elapsed}s")
