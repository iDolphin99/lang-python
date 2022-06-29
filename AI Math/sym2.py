# 수치미분 구현 

import sympy
import numpy as np

# f : function, 하나의 변수에 대한 funtion이 들어갈 것이냐
# x : 하나의 변수냐, 다변수냐(벡터)? 
# delta x = 0.001 (default setting)
# method -> 전방, 중앙 , forword, center 
def num_deriv (f, x, h=0.001, method="center") :
    # x의 타입을 확인하여 스칼라인지 벡터인지 확인
    # 스칼라를 (1,1)의 벡터로 표현 
    if type(x) in (float, int) :
        grad = [0.0] 
        x_ = [x]
        var_type = 'scalar'
    
    # 미분변수 크기만큼 벡터 초기화 
    else : 
        grad = np.zeros(x.shape)
        x_ = x.copy().astype('float32')
        var_type = 'vector'
        
    for i, xi in enumerate(x_) : 
        original_value = x_[i]
        
        # 전방 차분법 (분자의 왼쪽 항)
        if method == 'forword' : 
            x_[i] = original_value + h
        # 중앙 차분법
        else :
            x_[i] = original_value + (h/2)
        
        if var_type == 'saclar' :
            gradplus = f(x_[i])
        else : 
            gradplus = f(x_)
            
        # 전방 차분법 (분자의 오른쪽 항)
        if method == 'forward' :
            x_[i] = original_value
        else :
            x_[i] = original_value - (h/2)
            
        if var_type == 'saclar' :
            gradminus = f(x_[i])
        else : 
            gradminus = f(x_)
            
        # 평균변화율 계산 
        grad[i] = (gradplus - gradminus) / h 

x = sympy.Symbol('x')
f1= (x**2 + 2*x) * sympy.log(x)
#f2 = (x**2 + 2*x) * sympy.log(y)

print(num_deriv(f1, 1, h=0.001, method="forward"))
print(num_deriv(f1, 1, h=0.001, method="ceter"))    

# 직접미분을 통해 얻은 3.0이라는 값은 정화히 얻을 수 없다
# 3.0025...
# 2.99999...