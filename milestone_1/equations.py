# <a>x^2 + <b>x + <c> = 0

import cmath

eq = input('The equation: ')


coefficients = (eq.replace('x^2', " ").replace('x', " ").replace('=', " ")
                .replace('0', " ").replace(' ', "").replace('(', "")
                .replace(')', "").replace('+', ""))

a = int(coefficients[0])
b = int(coefficients[1])
c = int(coefficients[2:4])

print(f'a = {a}, b = {b}, c = {c}')

d = (b**2) - (4*a*c)

print(f'D = {d}')

x1 = ((-b-cmath.sqrt(d))/(2*a))
x2 = ((-b+cmath.sqrt(d))/(2*a))

print(f'Solutions: {x1}, {x2}')
