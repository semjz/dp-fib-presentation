import time

memo = dict()


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if not memo.get(n):
        memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


n = int(input())
start_time = time.perf_counter()
result = fib(n)
end_time = time.perf_counter()
time_elapsed = end_time - start_time
print(f"result:{result}, time elapsed: {time_elapsed}s")
