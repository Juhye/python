#!/usr/bin/env python
# coding: utf-8

# In[7]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { front-weight: bold !important;}</style>"))
display(HTML("<style>.container { width: 100% !important; )</style>"))


# # LATEX문법 
# ## 수학기호를 삽입 할 수 있는 문법
# $$ 레이텍 문법 $$
# $$ -> 두개 쓴 경우, 중앙 정렬 $$
# 
# $ 레이텍 문법 $  
# -> 하나만 쓴 경우, 왼쪽 정렬

# $ \alpha $
# 
# $$ y = x^3 + 2x^2 + x + 3 $$
# 

# # 파이썬의 산술식

# In[5]:


from sympy import Symbol, solve

k = Symbol('k')
equation = 2 * (k**2) - 50
solve(equation)


# In[8]:


a = input("값을 입력하세요: ")
b = input("값을 입력하세요: ")

print(f"a의 값은 {a} 이고, b의 값은 {b}입니다.")
a, b = b, a

print(f"바뀐 a의 값은 {a} 이고, 바뀐 b의 값은 {b}입니다.")


# In[11]:


conda install sympy


# In[12]:


pip list


# # 방정식 구현

# In[19]:


from sympy import Symbol, solve

x = Symbol('x') #  미지수 설정
x


# In[14]:


equation = 2*x - 6
equation


# In[15]:


solve(equation)


# In[4]:


# 연립 방정식
from sympy import Symbol, solve

x = Symbol('x')
y = Symbol('y') # Symbol 쓸때 s는 꼭 대문자여야한다..안그러면 에러남

equation1 = 3 * x + y - 2
equation2 = x - 2 * y -3

solve((equation1, equation2), dict = False)
      #list 형식으로 출력된다


# # 함수

# In[8]:


# 1차 함수
from sympy import Symbol, solve

x = Symbol('x')

fx = 3 * x - 2
fx

print(f"x = 1일때 함수값:   {fx.subs(x, 1)}")
print(f"x = 5일때 함수값:   {fx.subs(x, 5)}")
print(f"x = 10일때 함수값:   {fx.subs(x, 10)}")


# In[10]:


# 2차 함수

from sympy import Symbol, solve

x = Symbol('x')

fx = x**2 + 3*x + 5
fx

#함수식.subs(x,값)
print(f"x = 1일때 함수값:   {fx.subs(x, 1)}")
print(f"x = 5일때 함수값:   {fx.subs(x, 5)}")
print(f"x = 10일때 함수값:   {fx.subs(x, 10)}")


# In[12]:


print("오른쪽 정렬예제 {0:>20}".format("AAA"))
print("왼쪽 정렬예제 {0:<20}".format("AAA"))
print("가운데 정렬예제 {0:^20}".format("AAA"))


# In[14]:


# 1차 함수 그래프
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4, 5)
y = 2 * x
plt.plot(x,y)

y = 2 * x + 3
plt.plot(x,y)

y = 2 * x - 3
plt.plot(x,y)

plt.grid()
plt.show()


# In[17]:


# 2차 함수 그래프
x = np.linspace(-4, 4, 50)
#linspace 함수는 구간 내에 숫자 촘촘하게 세우는 함수. 처음, 끝 , 갯수 지정한다. 갯수에는 끝점 포함
y = x**2
plt.plot(x, y, label = 'g1')

y = 2*x**2
plt.plot(x, y, label = 'g2')

y = 4*x**2
plt.plot(x, y, label = 'g3')
plt.grid()
plt.legend(loc = 'upper left', ncol = 3)
        
plt.show()


# In[ ]:




