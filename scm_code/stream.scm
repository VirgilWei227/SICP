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

; ;; 使用示例
; (define nat-stream (naturals 0))  ; 创建自然数流
; (stream-take nat-stream 10)       ; 取出前10个自然数
; (stream-map (lambda (x) (* x x)) nat-stream)  ; 对自然数流中的每个元素求平方