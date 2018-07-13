
# https://vietjack.com/python/xu_ly_ngoai_le_trong_python.jsp

# Khối try-except trong Python
print("\nCode chay thanh cong")
try:
   fh = open("testfile", "w")
   fh.write("Day la mot kiem tra nho ve xu ly ngoai le!!")
except IOError:
   print ("Error: Khong tim thay file")
else:
   print ("Thanh cong ghi noi dung vao file")
   fh.close()

print("\nThong bao code loi")
try:
   fh = open("testfile", "r")
   fh.write("Day la mot kiem tra nho ve xu ly ngoai le!!")
except IOError:
   print ("Error: Khong tim thay file")
else:
   print ("Thanh cong ghi noi dung vao file")

# Khối try-finally trong Python
print("\nKhối try-finally trong Python")
try:
   fh = open("testfile", "b")
   fh.write("Day la mot kiem tra nho ve xu ly ngoai le!!")
except IOError:
   print ("Error: Khong tim thay file")
except:
   print ("Error: Meo biet loi gi")
else:
   print ("Thanh cong ghi noi dung vao file")
finally:
   print ("Code luôn dc thực thi")  # dù có hay k có exception thì ddoanjj code vẫn dc thực hiện


print("\nTham số của một Exception trong Python")
def temp_convert(var):
    try:
        return int(var)
    except Exception as agrument:
        print ("Error: ", agrument)
temp_convert("xyz");

print("\nTạo một Exception trong Python")
try:
    raise NameError("Name error")
except NameError as e:
    print (e)

print("\nCustom Exception trong Python")
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg

try:
   raise Networkerror("Bad hostname")
except Networkerror as e:
   print(e.args)