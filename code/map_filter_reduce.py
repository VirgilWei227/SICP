def remove(lst, x):
    return [i for i in lst if i != x]

def flatmap(fn, lst):
    return [y for x in lst for y in fn(x)]

def filter(fn, lst):
    return [x for x in lst if fn(x)]

def map(fn, lst):
    return [fn(x) for x in lst]

def permutations(lst):
    if not lst:
        return [[]]
    else:
        return flatmap(lambda x: map(lambda p: [x] + p, permutations(remove(lst, x))), lst)
    
def queens(board_size):
    def safe(queen, queens):
        return all(queen[0] != q[0] and queen[1] != q[1] and abs(queen[0] - q[0]) != abs(queen[1] - q[1]) for q in queens)
    
    def place_queen(k, queens):
        if k == 0:
            return queens
        else:
            return flatmap(lambda x: place_queen(k - 1, queens + [x]) if safe(x, queens) else [], [(k, y) for y in range(1, board_size + 1)])
    
    return place_queen(board_size, [])

if __name__ == '__main__':
    print(permutations([1, 2, 3]))
    print(queens(4))