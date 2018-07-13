
# Module trong Python, mỗi module tương ứng vs 1 file code
# https://vietjack.com/python/module_trong_python.jsp
print("Sử dụng lệnh import trong Python")
import addition
addition.add(10,20)
addition.add(30,40)

print("Sử dụng lệnh from…import trong Python")
from area import square,rectangle
square(10)
rectangle(2,5)

print("Sử dụng lệnh from…import* trong Python")
from area import *
square(10)
rectangle(2,5)
circle(5)
triangle(10,20)

print("Built-in Module trong Python")
import math
a=4.6
print (math.ceil(a))
print (math.floor(a))
b=9
print (math.sqrt(b))
print (math.exp(3.0))
print (math.log(2.0))
print (math.pow(2.0,3.0))
print (math.sin(0))
print (math.cos(0))
print (math.tan(45))\

import random
print (random.random())
print (random.randint(2,8))

print("\nPackage trong Python")
import Info.msg1
Info.msg1.msg1()
import Info.msg2 as msg
msg.msg2()