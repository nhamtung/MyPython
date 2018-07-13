
# Date & Time trong Python
# https://vietjack.com/python/date_time_trong_python.jsp
import time;  # Import time library
print("\nLấy Time hiện tại trong Python")
localtime = time.localtime(time.time())
print ("Thoi gian hien tai la :", localtime)

print("\nLấy Time đã được định dạng trong Python")
localtime = time.asctime( time.localtime(time.time()) )
print ("Thoi gian da duoc dinh dang la :", localtime)

print("\ncalendar Module trong Python")
import calendar
print ("Thang hien tai la: ")
cal = calendar.month(2014, 6)
print (cal)

print("\nHàm firstweekday(): Trả về ngày trong tuần đầu tiên. Theo mặc định là 0 mà xác định là Monday")
import calendar
print (calendar.firstweekday())

print("\nHàm isleap(year): Trả về true nếu năm đã cho là năm nhuận, nếu không là false")
import calendar
print (calendar.isleap(2000))

print("\nHàm monthcalendar(year,month): Trả về một list gồm các ngày trong tháng đã cho của năm dưới dạng các tuần")
import calendar
print (calendar.monthcalendar(2015,11))

print("\nHàm prmonth(year,month): In ra tháng đã cho của năm đã cung cấp")
import calendar
print (calendar.prmonth(2015,11))














