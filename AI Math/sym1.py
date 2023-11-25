# 직접미분 구현 

import sympy
import numpy as np

# 문자 선언 및 f 정의
x = sympy.Symbol('x')
f = (x**2 + 2*x) * sympy.log(x)

# sympy.diff를 통한 미분
df = sympy.diff(f, x)
print(sympy.simplify(df))

calculated_df = lambda x : (x + 2*(x+1)*np.log(x) + 2)
print(calculated_df(1))