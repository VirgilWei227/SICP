(define (map proc items)
    (if (null? items)
        '()
        (cons (proc (car items))
                (map proc (cdr items)))))

(define (square x) (* x x))

(map square (list 1 2 3 4 5))

(define (count-leaves x)
    (cond ((null? x) 0)
          ((not (pair? x)) 1)
          (else (+ (count-leaves (car x))
                   (count-leaves (cdr x))))))

(define (deep-reverse x)
    (cond ((null? x) x)
          ((not (pair? x)) x)
          (else (append (deep-reverse (cdr x))
                        (list (deep-reverse (car x)))))))

(define (fringe x)
    (cond ((null? x) '())
          ((not (pair? x)) (list x))
          (else (append (fringe (car x))
                        (fringe (cdr x))))))

(define (scale-tree tree factor)
    (map (lambda (sub-tree)
            (if (pair? sub-tree)
                (scale-tree sub-tree factor)
                (* sub-tree factor)))
         tree))