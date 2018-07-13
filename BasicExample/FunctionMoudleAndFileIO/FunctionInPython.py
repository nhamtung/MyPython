# Function trong Python
# https://vietjack.com/python/ham_trong_python.jsp
def printme( str ):
   "Chuoi nay duoc truyen vao trong ham"
   print (str)
   return
printme("I love you")

print("\nHàm return() trong Python")
# Phan dinh nghia ham o day
def sum( arg1, arg2 ):
   # Cong hai tham so va tra ve ket qua."
   total = arg1 + arg2
   print ("Ben trong ham : ", total)
   return total;
# Bay gio ban co the goi ham sum nay
total = sum( 10, 20 );
print ("Ben ngoai ham : ", total)

print("\nPhân biệt argument và parameter trong Python")
def addition(x, y):
    print (x + y)
x = 15
addition(x, 10)
addition(x, x)
y = 20
addition(x, y)

print("\nTruyền bởi tham chiếu vs bởi giá trị trong Python")
print("truyền tham chiếu: Tất cả parameter (argument) trong Python được truyền bởi tham chiếu")
def changeme( mylist ):
   "Thay doi list da truyen cho ham nay"
   mylist.append([1,2,3,4]);
   print ("Cac gia tri ben trong ham la: ", mylist)
   return
mylist = [10,20,30];
changeme( mylist );
print ("Cac gia tri ben ngoai ham la: ", mylist)

print("Truyền giá trị")
def changeme( mylist ):
   "Thay doi list da truyen cho ham nay"
   mylist = [1,2,3,4]; # Lenh nay gan mot tham chieu moi cho mylist
   print ("Cac gia tri ben trong ham la: ", mylist)
   return
mylist = [10,20,30];
changeme( mylist );
print ("Cac gia tri ben ngoai ham la: ", mylist)

print("\nTham số hàm trong Python")
print("Tham số bắt buộc trong Python")
def sum(a, b):
    c = a + b
    print (c)
sum(10, 20)

print("Tham số mặc định trong Python")
def msg(Id, Ten, Tuoi=21):
    print (Id)
    print (Ten)
    print (Tuoi)
    return
msg(Id=100, Ten='Hoang', Tuoi=20)
msg(Id=101, Ten='Thanh')

print("\nTham số từ khóa trong Python")
def msg(id,ten):
   print (id)
   print (ten)
   return
msg(id=100,ten='Hoang')
msg(ten='Thanh',id=101)

print("\nHàm với số tham số thay đổi trong Python")
def printinfo( arg1, *vartuple ):
   "In mot tham so da truyen"
   print ("Ket qua la: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;
printinfo( 10 )
printinfo( 70, 60, 50)

print("\nHàm nặc danh trong Python")
#Phan dinh nghia ham
square=lambda x1: x1*x1
#Goi square nhu la mot ham
print ("Binh phuong cua so la",square(10))