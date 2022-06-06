# what is computer science
与计算相关的研究

* 什么问题可以通过计算解决？可计算性
* 怎样解决这些问题
* 效率问题

# SICP

* 管理复杂性
    * 掌握抽象
* combining multiple ideas in large projects
* 计算机怎样解释程序语言

# python 基础
```python
    from math import pi
    radius = 10
    area, circ = pi * radius * radius, 2 * pi * radius
    from operator import, add, mul
```

## 函数定义
```python
    radius = 10
    def square(x):
        return mul(x, x)
    def sum_squares(x, y):
        return square(x) + square(y)
    # 可以直接捕获外部
    def area():
        retrun pi * radius * radius
```

## 表达式类型
* 简单表达式：Number or Numeral, name, string
* call expressions: Operator ans Operand

## 环境 Environment Diagrams
memory: 记录名字和变量函数的关系。sequence of frames

现在当前环境进行查找，找不到再向上一级进行查找，进入square后square优先代表一个变量。
```python
from operator import mul
def square(square):
    return mul(square, square)
square(-2)
```

## python: nonlocal
将外部函数变量捕获，以便在函数内使用。此时并没有新的变量产生，子函数对变量的修改会反应到外部函数。

**python的函数具有状态，类似于functor**
```python
def make_test_dice(*outcomes):
    """Return a die that cycles deterministically through OUTCOMES.
    >>> dice = make_test_dice(1, 2, 3)

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1

    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice
```

## 设计函数
文档字符串, help(func)显示文档字符串。
```python
def func():
    """ ........
    ......
    ......
    """
    return 0
```

## 测试与debug
```python
>>> assert fib(8) == 13, 'The 8th Fibonacci number should be 13'
>>> def fib_test():
        assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
        assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
        assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'
```

```python
>>> def sum_naturals(n):
        """Return the sum of the first n natural numbers.

        >>> sum_naturals(10)
        55
        >>> sum_naturals(100)
        5050
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total
```

```python
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""


def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

```

```python
python3 -m doctest file.py [-v]
```

### Error Types
* SyntaxError
* IndentationError: 缩进错误
* TypeError
* NameError: 变量名未定义等
* IndexError: out of range

# Side effects and Pure Functions
A side effect is when something happens as a result of calling a function besides just returning a value.

* pure function: just return values
* Non-pure function: have side effects

# Multiple Enviroments
函数调用->new environment

# Higher-Order Function

## Generalizing Patterns with Arguments

* Functions are first-class: Functions can be manipulated as values in our language.

* Higher-order function: A function that takes a function as an argument value or returns a function as a return value

```python
def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 8)
    Player 0 now has 10 and Player 1 now has 8
    >>> h3 = h2(10, 17)
    Player 0 now has 10 and Player 1 now has 17
    Player 1 takes the lead by 7
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say
```

# Lambda Expressions
Lambda Expressions are expressions that evaluate to functions.
```python
square = lambda x: x * x
square(4)
(lambda x: x * x)(3)
```

## python: Conditional Expressions(三目运算符？)
```
    <consequent> if <predicate> else <alternative>
```

```python
    # Relu
    lambda x: x if x > 0 else 0
```

# 应用序与正则序
* 先求值：应用序
* 先展开：正则序


# 递归与树形递归

## GCD（最大公约数）

求a，b的GCD，$r = a \% b$。

$GCD(a,b) = GCD(b,r)$

    Lame定理：如果欧几里得算法需要k步计算出一对整数的GCD，那么这对数中较小的数必然大于等于第k个斐波那契数

**证明**
$a = kb + r$，
假设$d$是$a,b$的一个公约数，
$r \div d = a \div d - kb \div d = 0$
所以$d$是$b, r$的一个公约数；

假设$d$是$b, r$的一个公约数，
$r\% d = (a - kd)\% d = a\% d - kb \%d = 0$，则$a \% d$为整数，
所以$d$是$a,b$的一个公约数。

```python
    from ucb import trace

    @trace
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 2) + fib(n - 1)
```

# Y组合子，匿名递归函数
$\lambda f. (\lambda x. f (x x))(\lambda x. f (x x))$
对于任意$\lambda f.$，$(\lambda x. f (x x))(\lambda x. f (x x))$，是$f$的不动点
$$
\begin{align*}
    &X = (\lambda x. f (x x))(\lambda x. f (x x))\\
    &X = f (x x)[x := \lambda x. f (x x)] \quad \beta-reduction\\
    &X = f((\lambda x. f (x x))(\lambda x. f (x x)))\\
    &X = f(X)
\end{align*}
$$
匿名递归阶乘
```python
    (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, k - 1)))
```

# 构造数据抽象

数据抽象的过程性（可以用过程构造数据）->消息传递
```python
    def cons(x, y):
        def dispatch(m):
            if m == 0:
                return x
            else:
                return y
        return dispatch


    def car(z):
        return z(0)
    def cdr(z):
        return z(1)
```

## 层次性数据和闭包性质
In general, an operation for combining data objects satisfies the closure property if the results of combining things with that operation can themselves be combined using the same operation.

### 序对表示序列
```
cons(1, cons(2，cons(3, cons(4, nil))))
```
### python sequence processing

#### List Comprehensions 
[\<map expression> for \<name> in \<sequence expression> if \<filter expression>]

```python
odds = [1, 3, 5, 7, 9]
[x + 1 for x in odds]

>>> [x for x in odds if 25 % x == 0]
[1, 5]
```

#### Aggregation
序列聚合成一个值
```python
>>> def divisors(n):
        return [1] + [x for x in range(2, n) if n % x == 0]
>>> divisors(4)
[1, 2]
>>> divisors(12)
[1, 2, 3, 4, 6]

>>> [n for n in range(1, 1000) if sum(divisors(n)) == n]
[6, 28, 496]
```

#### 序列操作的高阶函数形式
``` python
# List Comprehensions
>>> def apply_to_all(map_fn, s):
        return [map_fn(x) for x in s]
# List filter
>>> def keep_if(filter_fn, s):
        return [x for x in s if filter_fn(x)]
# aggregation
>>> def reduce(reduce_fn, s, initial):
        reduced = initial
        for x in s:
            reduced = reduce_fn(reduced, x)
        return reduced
```

apply_to_all -> map
keep_if -> filter
```python
>>> apply_to_all = lambda map_fn, s: list(map(map_fn, s))
>>> keep_if = lambda filter_fn, s: list(filter(filter_fn, s))

>>> from functools import reduce
>>> from operator import mul
>>> def product(s):
        return reduce(mul, s)
>>> product([1, 2, 3, 4, 5])
120
```

#### Membership 与 Slicing
```python
# membership
>>> digits
[1, 8, 2, 8]
>>> 2 in digits
True
>>> 1828 not in digits
True

# slicing
# [Initial : End : IndexJump]
>>> digits[0:2]
[1, 8]
>>> digits[1:]
[8, 2, 8]
# reverse 
digits[::-1]
```

### Python Trees
```python
>>> def tree(root_label, branches=[]):
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [root_label] + list(branches)
>>> def label(tree):
        return tree[0]
>>> def branches(tree):
        return tree[1:]

>>> def is_tree(tree):
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
>>> def is_leaf(tree):
        return not branches(tree)

```

### Python Dictionary
```python
words = {
    "más": "more",
    "otro": "other",
    "agua": "water"
}

insects = {"spiders": 8, "centipedes": 100, "bees": 6}
for name in insects:
    print(insects[name])
```

#### Dictionary comprehensions
```python
{<key exp>: <value exp> for <name> in <iter exp> if <filter exp>}
```

```clojure
(define (deep_reverse tree)
    (define (deep_reverse_it tree re)
        (cond ((null? tree)
                re)
              (else 
                (deep_reverse_it (cdr tree)
                    (cons (if (pair? (car tree))
                              (deep_reverse (car tree))
                              (car tree))
                          re)))))
    (deep_reverse_it tree '()))
```

#### C++的map和filter
```C++
int main()
{
    auto const ints = {0,1,2,3,4,5};
    auto even = [](int i) { return 0 == i % 2; };
    auto square = [](int i) { return i * i; };
 
    // "pipe" syntax of composing the views:
    for (int i : ints | std::views::filter(even) | std::views::transform(square)) {
        std::cout << i << ' ';
    }
 
    std::cout << '\n';
 
    // a traditional "functional" composing syntax:
    for (int i : std::views::transform(std::views::filter(ints, even), square)) {
        std::cout << i << ' ';
    }
    std::cout << std::endl;
    return 0;
}
```

### 序列操作

#### filter
```clojure
(define (filter predicate sequence)
    (cond ((null? sequence) nil)
          ((predicate (car sequence))
           (cons (car sequence)
                 (filter predicate (cdr sequence))))
          (else (filter predicate (cdr sequence)))))
```

#### fold_left and fold_right
```clojure
(define (reverse sequence)
    (fold_right (lambda (x y)
                    (cons y x))
                '()
                sequence))

(define (reverser sequence)
    (fold_right (lambda (x y) 
                    (append y (list x)))
                '()
                sequence))
```

## 可加性
基于类型的分派不具有可加性

数据导向or消息传递

### 数据导向
将\<op>和\<type>建表，通过
```clojure
(put <op> <type> <item>)
(get <op> <type>)
```
实现分发

## 不同类型数据的组合

强制->类型转换

层次->类型塔（继承）