(define (sum term a next b)
    (if (> a b)
        0
        (+ (term a)
           (sum term (next a) next b))))

(define (inc n) (+ n 1))
(define (cube x) (* x x x))
(define (sum-cubes a b)
    (sum cube a inc b))

(define (identity x) x)
(define (sum-integers a b)
    (sum identity a inc b))

(define (pi-sum a b)
    (define (pi-term x)
        (/ 1.0 (* x (+ x 2))))
    (define (pi-next x)
        (+ x 4))
    (sum pi-term a pi-next b))

(define (integral f a b dx)
    (define (add-dx x) (+ x dx))
    (* (sum f (+ a (/ dx 2.0)) add-dx b)
       dx))

(define (sum-iter term a next b)
    (define (iter a result)
        (if (> a b)
            result
            (iter (next a) (+ (term a) result))))
    (iter a 0))

(define (product term a next b)
    (if (> a b)
        1
        (* (term a)
           (product term (next a) next b))))

(define (product-iter term a next b)
    (define (iter a result)
        (if (> a b)
            result
            (iter (next a) (* (term a) result))))
    (iter a 1))

(define (factorial n)
    (define (identity x) x)
    (define (inc n) (+ n 1))
    (product-iter identity 1 inc n))

(define (accumulate combiner null-value term a next b)
    (if (> a b)
        null-value
        (combiner (term a)
                  (accumulate combiner null-value term (next a) next b))))

(define (sum-accumulate term a next b)
    (accumulate + 0 term a next b))

(define (product-accumulate term a next b)
    (accumulate * 1 term a next b))

(define (accumulate-iter combiner null-value term a next b)
    (define (iter a result)
        (if (> a b)
            result
            (iter (next a) (combiner (term a) result))))
    (iter a null-value))

(define (sum-accumulate-iter term a next b)
    (accumulate-iter + 0 term a next b))

(define (product-accumulate-iter term a next b)
    (accumulate-iter * 1 term a next b))

(define (factorial-iter-accumulate n)
    (define (identity x) x)
    (define (inc n) (+ n 1))
    (product-accumulate-iter identity 1 inc n))