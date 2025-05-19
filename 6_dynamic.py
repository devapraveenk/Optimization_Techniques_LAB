# Method 1
def fibo(n):
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return (fib, fib[n])


n = int(input())
num, seq = fibo(n)
print("NUMBER:", num)
print("SEQUENCE:", seq)


# Method 2
class Fibonacci(dict):
    def _missing_(self, n):
        if n <= 1:
            self[n] = n
        else:
            self[n] = self[n - 1] + self[n - 2]
        return self[n]


Fib = Fibonacci()
N = Fib[9]
print(N)
