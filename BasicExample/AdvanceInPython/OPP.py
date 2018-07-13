
# https://vietjack.com/python/khai_niem_huong_doi_tuong_trong_python.jsp

print("\n TẠO CÁC LỚP TRONG PYTHON")
class Sinhvien:
    'Class cơ sở chung cho tat ca sinh vien'
    svCount = 0
    def __init__(self, ten, hocphi):  #constructor
        self.ten = ten
        self.hocphi = hocphi
        Sinhvien.svCount += 1

    def displayCount(self):
        print ("Tong so Sinh vien %d" % Sinhvien.svCount)

    def displaySinhvien(self):
        print ("Ten : ", self.ten, ", Hoc phi: ", self.hocphi)


"Lenh nay tao doi tuong dau tien cua lop Sinhvien"
sv1 = Sinhvien("Hoang", 4000000)
"Lenh nay tao doi tuong thu hai cua lop Sinhvien"
sv2 = Sinhvien("Huong", 4500000)

sv1.displaySinhvien()
sv2.displaySinhvien()
print ("Tong so Sinh vien %d" % Sinhvien.svCount)

sv1.tuoi = 21  # Them mot thuoc tinh 'tuoi'.
sv1.tuoi = 20  # Sua doi thuoc tinh 'tuoi'.
del sv1.tuoi  # Xoa thuoc tinh 'tuoi'.

hasattr(sv1, 'tuoi')  #Truy cập thuộc tính của đối tượng. Tra ve true neu thuoc tinh 'tuoi' ton tai
# getattr(sv1, 'tuoi')  #Kiểm tra xem một thuộc tính có tồn tại hay không. Tra ve gia tri cua thuoc tinh 'tuoi'
setattr(sv1, 'tuoi', 20)  #Thiết lập một thuộc tính. Nếu thuộc tính không tồn tại, thì nó sẽ được tạo. Thiet lap thuoc tinh 'tuoi' la 20
delattr(sv1, 'tuoi')  # Xoa thuoc tinh 'tuoi'

print("\nCÁC THUỘC TÍNH CÓ SẴN CHO CLASS TRONG PYTHON")
print ("Sinhvien.__doc__:", Sinhvien.__doc__)
print ("Sinhvien.__name__:", Sinhvien.__name__)
print ("Sinhvien.__module__:", Sinhvien.__module__)
print ("Sinhvien.__bases__:", Sinhvien.__bases__)
print ("Sinhvien.__dict__:", Sinhvien.__dict__)

print("\nHỦY ĐỐI TƯỢNG TRONG PYTHON")
class Point:
   def __init( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3)) # in id cua doi tuong
del pt1
del pt2
del pt3


print("\nKẾ THỪA CLASS TRONG PYTHON")
class Parent:        # dinh nghia lop cha
   parentAttr = 100
   def __init__(self):
      print ("Goi constructor cua lop cha")
   def parentMethod(self):
      print ('Goi phuong thuc cua lop cha')
   def setAttr(self, attr):
      Parent.parentAttr = attr
   def getAttr(self):
      print ("Thuoc tinh cua lop cha :", Parent.parentAttr)

class Child(Parent): # dinh nghia lop con
   def __init__(self):
      print ("Goi constructor cua lop con")
   def childMethod(self):
      print ('Goi phuong thuc cua lop con')

c = Child()          # instance cua lop con
c.childMethod()      # lop con goi phuong thuc cua no
c.parentMethod()     # goi phuong thuc cua lop cha
c.setAttr(200)       # tiep tuc goi phuong thuc cua lop cha
c.getAttr()          # tiep tuc goi phuong thuc cua lop cha

print("\nGHI ĐÈ PHƯƠNG THỨC TRONG PYTHON")
class Parent:        # dinh nghia lop cha
   def myMethod(self):
      print ('Goi phuong thuc cua lop cha')
class Child(Parent): # dinh nghia lop con
   def myMethod(self):
      print ('Goi phuong thuc cua lop con')
c = Child()          # instance cua lop con
c.myMethod()         # lop con goi phuong thuc duoc ghi de

print("\nNẠP CHỒNG TOÁN TỬ TRONG PYTHON")
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print (v1 + v2)

print("\n DATA HIDING IN PYTHON")
class JustCounter:
    __secretCount = 0
    def count(self):
        self.__secretCount += 1
        print ("private: ", self.__secretCount)
counter = JustCounter()
counter.count()
try:
    print (counter.__secretCount)
except Exception as ex:
    print("Error: ", ex)




