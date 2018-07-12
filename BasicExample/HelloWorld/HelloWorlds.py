
print ("Hello World! \nMy full name is Nham Van Tung")

# this command for comment
"""This is 
multiline comment"""

#trong Python ket thuc 1 dong la het 1 lenh
x = "x"
y = "y"
z = "z"
total = x + \
    y + z
print("Total = " + total)

# Trong Python khong co dau {}, de xac dinh cau lenh cung 1 khoi dua vao do thut dau dong
flag = 1
if flag == 1:
    x = "a"
    print("x = " + x)

# Cach dat ten 1 so bien
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print("word = " + word)
print("sentence = " + sentence)
print("paragraph = " + paragraph)
print("days[3] = " + days[3])

# cac lenh da dong tren 1 dong don
import sys; x = 'foo'; sys.stdout.write(x + '\n')


##############################################
# Cac kieu bien trong Python
print("\n")

# Gán các giá trị cho biến trong Python
a = 20          # Mot phép gan so nguyen
b   = 100.0       # Mot so thuc
ten    = "Hoang"       # Mot chuoi

print (a)
print (b)
print (ten)

# Phép đa gán (multiple assignment) trong Python
a,b,c=5,10,15
print (a)
print (b)
print (c)


#####################################################
print("\n")
# Toán tử trong Python

# Phép lấy số mũ
x = 2**3
print(x)

# Toán tử gán trong Python
x = 13; x += 3; print(x)
x = 13; x -= 3; print(x)
x = 13; x /= 3; print(x)
x = 13; x *= 3; print(x)
x = 13; x %= 3; print(x)
x = 13; x **= 3; print(x)
x = 13; x //= 3; print(x)

# Toán tử logic trong Python
a=5>4 and 3>2
print (a)
b=5>4 or 3<2
print (b)
c=not(5>4)
print (c)

# Toán tử thao tác bit trong Python
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b;        # 12 = 0000 1100
print("Dong 1 - Gia tri cua c la ", c)
c = a | b;        # 61 = 0011 1101
print("Dong 2 - Gia tri cua c la ", c)
c = a ^ b;        # 49 = 0011 0001
print("Dong 3 - Gia tri cua c la ", c)
c = ~a;           # -61 = 1100 0011
print("Dong 4 - Gia tri cua c la ", c)
c = a << 2;       # 240 = 1111 0000
print("Dong 5 - Gia tri cua c la ", c)
c = a >> 2;       # 15 = 0000 1111
print("Dong 6 - Gia tri cua c la ", c)

# Toán tử membership trong Python
"""Toán tử membership trong Python kiểm tra xem biến này có nằm trong dãy (có là một trong các thành viên của dãy) hay không"""
a=10
b=20
list=[10,20,30,40,50];
if (a in list):
    print("a la trong list da cho")
else:
    print("a la khong trong list da cho")
if(b not in list):
    print("b la khong trong list da cho")
else:
    print("b la trong list da cho")

# Toán tử identify trong Python
"""so sánh các vị trí ô nhớ của hai đối tượng"""
a=20
b=20
if( a is b):
	print ("a,b co cung identity")
else:
	print ("a, b la khac nhau")
b=10
if( a is not b):
	print ("a,b co identity khac nhau")
else:
	print ("a,b co cung identity")


