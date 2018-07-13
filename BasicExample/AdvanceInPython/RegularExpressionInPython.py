
# https://vietjack.com/python/regular_expression_trong_python.jsp

print("\nHÀM MATCH TRONG PYTHON: so khớp pattern với string với các flag tùy ý")
import re
str = "Hoc Python la de hon hoc Java?"
matchObj = re.match( r'(.*) la (.*?) .*', str, re.M|re.I)
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("Khong co ket noi!!")

print("\nHÀM SEARCH TRONG PYTHON: tìm kiếm cho sự xuất hiện đầu tiên của pattern bên trong string với các flags tùy ý")
import re
line = "Hoc Python la de hon hoc Java?";
searchObj = re.search( r'(.*) la (.*?) .*', line, re.M|re.I)
if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Khong tim thay!!")

print("\nPHÂN BIỆT MATCH VÀ SEARCH: match để kiểm tra chỉ một kết nối tại phần đầu của chuỗi, trong khi search tìm kiếm một kết nối ở bất cứ đâu trong chuỗi")
import re
line = "Hoc Python la de hon hoc Java?";
matchObj = re.match(r'thon', line, re.M | re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("Khong co ket noi!!")
searchObj = re.search(r'thon', line, re.M | re.I)
if searchObj:
   print("search --> searchObj.group() : ", searchObj.group())
else:
   print("Khong tim thay!!")

print("\nTÌM KIẾM VÀ THAY THẾ TRONG PYTHON: hàm sub")
import re
phone = "01633-810-628 # Day la so dien thoai"
# Xoa cac comment
num = re.sub(r'#.*$', "", phone)
print ("So dien thoai : ", num)
# Xoa cac ky tu khong phai ky so
num = re.sub(r'\D', "", phone)
print ("So dien thoai : ", num)