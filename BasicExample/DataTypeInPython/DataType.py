
# https://vietjack.com/python/number_trong_python.jsp

# Number
x = 3

import math
print(math.sqrt(4))

# String
print ("\nTruy cập các giá trị trong String:")
var1 = 'Hello World!'
var2 = "Python Programming"
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

print ("\nCập nhật String trong Python:")
var1 = 'Hello World!'
print ("Chuoi hien tai la :- ", var1[:6] + 'Python')

print("\nToán tử lặp chuỗi:")
print(5*"Hoang")

print("\nToán tử định dạng chuỗi trong Python")
print ("Ten toi la %s va toi nang %d kg!" % ('Hoang', 71))

print("\nTrích dẫn tam (triple quote) trong Python")
para_str = """day la mot chuoi day gom nhieu dong 
va gom mot so ky tu khong in duoc chang han nhu
TAB ( \t ) chung se duoc hien thi dung nguyen van nhu the."""
print (para_str)

print ('C:\\nowhere')
print (r'C:\\nowhere')
print (u'Hello, world!')

# List
print ("\nKhai bao List")
list1 = ['vatly', 'hoahoc', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

print("\nNối List")
list1=[10,20]
list2=[30,40]
list3=list1+list2
print(list3)

print("\n Lặp List")
list = [10,20]
print(list*2)

print("\nCập nhật List trong Python")
list = ['vatly', 'hoahoc', 1997, 2000];
print ("Gia tri co san tai chi muc thu 2 : ")
print (list[2])
list[2] = 2001;
print ("Gia tri moi tai chi muc thu 2 : ")
print (list[2])

print("\nPhụ thêm phần tử vào cuối một List")
list1=[10,"hoang",'z']
print ("Cac phan tu cua List la: ")
print (list1)
list1.append(10.45)
print ("Cac phan tu cua List sau khi phu them la: ")
print (list1)

print("\nXóa phần tử trong List")
list1 = ['vatly', 'hoahoc', 1997, 2000];
del list1[2];
print ("Cac phan tu cua List sau khi xoa gia tri tai chi muc 2 : ")
print (list1)
del list1[0:2]
print ("Cac phan tu cua List sau khi xoa: ")
print (list1)

# Tuple
print("\nKhai bao Tuple")
tup1 = ();
tup2 = (50,);
tupl1='a','hoang',10.56
tupl2=tupl1,(10,20,30)
print (tupl1)
print (tupl2)

print("\nTruy cập các giá trị trong tuple trong Python")
tup1 = ('vatly', 'hoahoc', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

print("\nCác hoạt động cơ bản trên tuple trong Python")
data1=(1,2,3,4)
data2=('x','y','z')
data3=data1+data2
print (data3)

tuple1=(10,20,30);
print (tuple1*2)

print("\nXóa các phần tử của tuple trong Python")
data=(10,20,'hoang',40.6,'z')
print (data)
#del data      #se xoa du lieu cua tuple
print (data)	#se hien thi mot error boi vi tuple da bi xoa

print("\nTập hợp đối tượng mà không có dấu giới hạn")
"""Bất kỳ tập hợp nào gồm nhiều đối tượng, được phân biệt bởi dấu phảy, 
được viết mà không có các biểu tượng nhận diện (chẳng hạn như dấu ngoặc vuông cho List, dấu ngoặc đơn cho Tuple, …) 
thì Python mặc định chúng là Tuple"""
print ('abc', -4.24e93, 18+6.6j, 'xyz')
x, y = 1, 2;
print ("Gia tri cua x , y : ", x,y)

# Dictionary
print("\nKhai bao Dictionary")
data={100:'Hoang' ,101:'Nam' ,102:'Binh'}
print (data)

print("\nTruy cập các giá trị trong Dictionary trong Python")
data1={'Id':100, 'Ten':'Thanh', 'Nghenghiep':'Developer'}
data2={'Id':101, 'Ten':'Chinh', 'Nghenghiep':'Trainer'}
print ("Id cua nhan vien dau tien la",data1['Id'])
print ("Id cua nhan vien thu hai la",data2['Id'])
print ("Ten cua nhan vien dau tien la:",data1['Ten'])
print ("Nghe nghiep cua nhan vien thu hai la:",data2['Nghenghiep'])

print("\nCập nhật Dictionary trong Python")
data1={'Id':100, 'Ten':'Thanh', 'Nghenghiep':'Developer'}
data2={'Id':101, 'Ten':'Chinh', 'Nghenghiep':'Trainer'}
data1['Nghenghiep']='Manager'
data2['Mucluong']=17000000
data1['Mucluong']=12000000
print (data1)
print (data2)

print("\nXóa phần tử từ Dictionary trong Python")
data={100:'Hoang', 101:'Thanh', 102:'Nam'}
del data[102]
print (data)



