def fib_seq(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a*k + b
        print(b)

fib_seq(3, 3)
fib_seq(4, 3)
fib_seq(5, 3)
