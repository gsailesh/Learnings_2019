'''
Efficient Fibonacci computation
'''

d = {1:1, 2:2}

def fib_efficient(n, d=d):
    if n in d:
        return d[n]

    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans


print(fib_efficient(640,d))
print(d)