import sympy

def differentiate(expression, variable):
    x = sympy.symbols(variable)
    expr = sympy.sympify(expression)
    derivative = sympy.diff(expr, x)
    return derivative


if __name__ == "__main__":
    # Example usage
    expression = 'x**2 + 2*x - 3'
    variable = 'x'
    result = differentiate(expression, variable)
    print(result)   