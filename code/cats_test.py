a = ["testing", "tsking", "fasting"]
diff_fun = lambda w1, w2: abs(len(w1) - len(w2))

print(min(a, key=lambda s: diff_fun(s, 'tosting')))
