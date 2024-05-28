# class memorize:
#     def __init__(self, func):
#         self.func = func
#         self.cache = {}

#     def __call__(self, *args):
#         if args not in self.cache:
#             self.cache[args] = self.func(*args)
#         return self.cache[args]

def memorize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

# @memorize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    # 统计运行时间
    import time
    start = time.time()
    print(fib(35))
    print('Time: ', time.time()-start)

    fib = memorize(fib)
    start = time.time()
    print(fib(35))
    print('Time: ', time.time()-start)
    