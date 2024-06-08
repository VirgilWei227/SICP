;; 定义流的构造函数和选择器
(define (cons-stream head tail)
  (cons head (delay tail)))

(define (stream-car stream)
  (car stream))

(define (stream-cdr stream)
  (force (cdr stream)))

;; 创建无限自然数流
(define (naturals n)
  (cons-stream n (lambda () (naturals (+ n 1)))))

(define (stream-ref stream n)
  (if (= n 0)
      (stream-car stream)
      (stream-ref (stream-cdr stream) (- n 1))))

;; 访问和操作流
;; 取出流的前N个元素
(define (stream-take stream n)
  (if (= n 0)
      '()
      (cons (stream-car stream)
            (stream-take (stream-cdr stream) (- n 1)))))

;; 对流中的每个元素应用函数
(define (stream-map proc stream)
  (if (eq? stream '())  ; 检查流是否为空
      '()
      (cons-stream (proc (stream-car stream))
                   (lambda () (stream-map proc (stream-cdr stream))))))

(define (ones)
  (cons-stream 1 ones))

(define (integers)
  (cons-stream 1 (stream-map (lambda (x) (+ x 1)) integers)))

(define (add-streams s1 s2)
  (stream-map + s1 s2))

(define (scale-stream stream factor)
  (stream-map (lambda (x) (* x factor)) stream))

(define (fibs
  (cons-stream 0
               (cons-stream 1
                            (add-streams (stream-cdr fibs) fibs)))))

(define (stream-filter pred stream)
  (cond ((eq? stream '()) '())
        ((pred (stream-car stream))
         (cons-stream (stream-car stream)
                      (lambda () (stream-filter pred (stream-cdr stream)))))
        (else (stream-filter pred (stream-cdr stream)))))

(define (mul-streams s1 s2)
  (stream-map * s1 s2))

(define (div-streams s1 s2)
  (stream-map / s1 s2))

(define (factorials 
  (cons-stream 1
               (mul-streams (naturals 1) factorials))))

(define (partial-sums stream)
  (cons-stream (stream-car stream)
               (add-streams (stream-cdr stream)
                            (partial-sums stream))))

(define S (cons-stream 1 (merge (scale-stream S 2) (merge (scale-stream S 3) (scale-stream S 5)))))

(define (integrade-series s)
  (mul-streams s (div-streams ones integers)))
  
(define (merge s1 s2)
  (cond ((eq? s1 '()) s2)
        ((eq? s2 '()) s1)
        (else (if (< (stream-car s1) (stream-car s2))
                  (cons-stream (stream-car s1) (merge (stream-cdr s1) s2))
                  (cons-stream (stream-car s2) (merge s1 (stream-cdr s2)))))))

(define (exp-series)
  (cons-stream 1 (integrade-series exp-series)))

(define (cos-series)
  (cons-stream 1 (integrade-series (scale-stream (stream-cdr sin-series) -1))))

(define (sin-series)
  (cons-stream 0 (integrade-series cos-series)))

(define (mul-series s1 s2)
  (cons-stream (* (stream-car s1)
                  (stream-car s2))
               (add-streams (mul-streams (stream-cdr s1)
                                         (stream-cdr s2))
                            (mul-series s1 s2))))
; ;; 使用示例
; (define nat-stream (naturals 0))  ; 创建自然数流
; (stream-take nat-stream 10)       ; 取出前10个自然数
; (stream-map (lambda (x) (* x x)) nat-stream)  ; 对自然数流中的每个元素求平方