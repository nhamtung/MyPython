# https://vietjack.com/python/file_io_trong_python.jsp

print("In kết quả ra màn hình trong Python")

# print("\nĐọc input từ bàn phím trong Python")
# str = input("Nhap dau vao cua ban: ");
# print ("Dau vao da nhan la : ", str)

print("\nLàm việc với File trong Python")
print("Đóng/Mở, Đọc/Ghi file trong Python")
obj=open("Tung.txt","w")
obj.write("Tao la Nham Van Tung")
obj.close()
obj1=open("Tung.txt","r")
s=obj1.read()
print (s)
obj1.close()
obj2=open("Tung.txt","r")
s1=obj2.read(20)
print (s1)
obj2.close()

fo = open("Tung.txt", "wb")
print ("Ten cua file la: ", fo.name)
print ("File da duoc dong hay chua : ", fo.closed)
print ("Che do mode la : ", fo.mode)
#print ("Softspace la : ", fo.softspace)
fo.close()

print("\nRename/Delete file trong Python")
import os
os.rename( "Tung.txt", "test2.txt" )# Thay ten tu Tung.txt thanh test2.txt
os.remove("test2.txt")

print("\nVị trí File trong Python")
# Mo mot file
fo = open("foo.txt", "w")
fo.write("I am Tung")
fo = open("foo.txt", "r")
str = fo.read(10);
print ("Chuoi da doc la : ", str)

# Kiem tra con tro hien tai
position = fo.tell();
print ("Con tro file hien tai : ", position)

position = fo.seek(5, 0);#Dat lai vi tri con tro tai vi tri ban dau mot lan nua
position = fo.tell();
print ("Con tro file hien tai : ", position)
fo.close()# Dong file da mo

print("\nThư mục trong Python")
import os
folder = os.getcwd() # Lenh nay se cung cap vi tri thu muc hien tai
print(folder)

os.mkdir("test")# Tao mot thu muc la "test"
os.rmdir("test") # Xoa thu muc test

os.chdir("Info")# Thay doi mot thu muc toi "/home/newdir"
os.mkdir("readme")# Tao mot thu muc la "test"
os.rmdir("readme") # Xoa thu muc test