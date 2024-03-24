(define last-pair
  (lambda (l)
    (if (null? (cdr l))
        l
        (last-pair (cdr l)))))

(define append
  (lambda (lst1 lst2)
    (if (null? lst1)
        lst2
        (cons (car lst1) (append (cdr lst1) lst2)))))

(define (reverse lst)
  (if (null? lst)
      lst
      (append (reverse (cdr lst)) (list (car lst)))))
  
(define (same-parity x . lst)
  (define (even? x) (= (remainder x 2) 0))
  (define (odd? x) (not (even? x)))
  (define (iter l)
    (if (null? l)
        '()
        (if (even? x)
            (if (even? (car l))
                (cons (car l) (iter (cdr l)))
                (iter (cdr l)))
            (if (odd? (car l))
                (cons (car l) (iter (cdr l)))
                (iter (cdr l)))))
    )
  (cons x (iter lst)))