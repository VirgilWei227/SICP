(define (map proc items)
    (if (null? items)
        '()
        (cons (proc (car items))
                (map proc (cdr items)))))

(define (filter pred items)
    (cond ((null? items) '())
          ((pred (car items))
            (cons (car items)
                    (filter pred (cdr items))))
          (else (filter pred (cdr items)))))

(define (accumulate op initial sequence)
    (if (null? sequence)
        initial
        (op (car sequence)
            (accumulate op initial (cdr sequence)))))

(define (flatmap proc seq)
    (accumulate append '() (map proc seq)))

(define (enumerate-interval low high)
    (if (> low high)
        '()
        (cons low (enumerate-interval (+ low 1) high))))

(define (enumerate-tree tree)
    (cond ((null? tree) '())
          ((not (pair? tree)) (list tree))
          (else (append (enumerate-tree (car tree))
                        (enumerate-tree (cdr tree))))))

(define (sum-odd-squares tree)
    (accumulate +
                0
                (map (lambda (x) (* x x))
                    (filter odd?
                            (enumerate-tree tree)))))

(define (fib n)
    (if (= n 0)
        0
        (if (= n 1)
            1
            (+ (fib (- n 1))
                (fib (- n 2))))))

(define (even-fibs n)
    (accumulate cons
                '()
                (filter even?
                        (map fib
                            (enumerate-interval 0 n)))))

; ;; Test case for sum-odd-squares
; (define tree1 '(1 (2 3) (4 (5 6))))
; (define tree2 '(1 (2 (3 (4 (5 (6)))))))
; (define tree3 '())
; (define tree4 '(1))
; (define tree5 '((2) (3) (4) (5) (6)))

; (displayln (sum-odd-squares tree1)) ; Expected output: 91
; (displayln (sum-odd-squares tree2)) ; Expected output: 91

; ;; Test case for even-fibs
; (displayln (even-fibs 0)) ; Expected output: ()
; (displayln (even-fibs 1)) ; Expected output: (0)
; (displayln (even-fibs 2)) ; Expected output: (0 2)

(define (remove x s)
    (filter (lambda (y) (not (= x y))) s))


(define (permutations s)
    (if (null? s)
        (list '())
        (flatmap (lambda (x)
                    (map (lambda (p) (cons x p))
                        (permutations (remove x s))))
                s)))

(define (adjoin-position new-row k rest-of-queens)
    (cons (cons new-row k) rest-of-queens))

(define (safe? k positions)
    (let ((queen (car positions))
          (rest-of-queens (cdr positions)))
        (define (iter rest-of-queens)
            (if (null? rest-of-queens)
                #t
                (let ((other (car rest-of-queens)))
                    (if (or (= (car queen) (car other))
                            (= (cdr queen) (cdr other))
                            (= (- (car queen) (car other))
                               (- (cdr queen) (cdr other)))
                            (= (- (car queen) (car other))
                               (- (cdr other) (cdr queen))))
                        #f
                        (iter (cdr rest-of-queens))))))
        (iter rest-of-queens)))

(define (queens board-size)
    (define empty-board '())
    (define (queen-cols k)
        (if (= k 0)
            (list empty-board)
            (filter
                (lambda (positions) (safe? k positions))
                (flatmap
                    (lambda (rest-of-queens)
                        (map (lambda (new-row)
                                (adjoin-position new-row k rest-of-queens))
                            (enumerate-interval 1 board-size)))
                    (queen-cols (- k 1))))))
    (queen-cols board-size))

(define (corner-split painter n)
    (if (= n 0)
        painter
        (let ((up (up-split painter (- n 1)))
              (right (right-split painter (- n 1)))
              (bottom (bottom-split painter (- n 1))))
            (let ((top-left (beside (below center center) center))
                  (top-right (beside (below center center) center))
                  (corner (corner-split center (- n 1))))
                (below (beside top-left top-right)
                        (beside bottom-left bottom-right))))))