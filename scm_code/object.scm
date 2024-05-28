(define (make-accumulator initial-value)
  (let ((sum initial-value))
    (lambda (x)
      (set! sum (+ sum x))
      sum)))

(define A (make-accumulator 5))

(define (make-monitored f)
  (let ((counter 0))
    (lambda (x)
      (set! counter (+ counter 1))
      (display "Calls: ")
      (display counter)
      (newline)
      (f x))))

(define (random-in-range low high)
  (let ((range (- high low)))
    (+ low (random range))))`