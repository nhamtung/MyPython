# if...else...
var = 100
if var == 200:
   print("1 - Nhan mot gia tri true")
   print(var)
elif var == 150:
   print("2 - Nhan mot gia tri true")
   print(var)
elif var == 100:
   print("3 - Nhan mot gia tri true")
   print (var)
else:
   print ("4 - Nhan mot gia tri false")
   print (var)
print ("Good bye!\n")

# while...
count = 0
while (count < 9):
   print('So thu tu cua ban la:', count)
   count = count + 1
print ("Good bye!")

# var = 1
# print("để thoát khỏi nó thì bạn cần nhấn phím CTRL+C")
# while var == 1 :  # Lenh nay tao mot vong lap vo han
#    num = raw_input("Hay nhap mot so  :")
#    print ("So da nhap la: ", num)
# print ("Good bye!")

count = 0
while count < 5:
   print (count, " la nho hon 5")
   count = count + 1
else:
   print (count, " la khong nho hon 5")

# for...
for letter in 'Python':     # Vi du dau tien
   print ('Chu cai hien tai :', letter)

qua = ['chuoi', 'tao',  'xoai']
for index in range(len(qua)):      # Vi du thu hai
   print ('Ban co thich an :', qua[index])
print ("Good bye!")

for num in range(10,20):  #de lap tu 10 toi 20
   for i in range(2,num): #de lap tren cac thua so cua mot so
      if num%i == 0:      #de xac dinh thua so dau tien
         j=num/i          #de uoc luong thua so thu hai
         print ('%d la bang %d * %d' % (num,i,j))
         break #de di chuyen toi so tiep theo, la vong FOR dau tien
   else:                  # else la mot phan cua vong lap
      print (num, 'la so nguyen to')

# break...
"""Lệnh này kết thúc vòng lặp hiện tại và truyền điều khiển tới cuối vòng lặp"""
for letter in 'Python':  # Vi du thu nhat
    if letter == 'h':
        break
    print ('Chu cai hien tai :', letter)
var = 10  # Vi du thu hai
while var > 0:
    print ('Gia tri bien hien tai la :', var)
    var = var - 1
    if var == 5:
        break
print ("Good bye!")

# continue...
""" trả về điều khiển tới phần ban đầu của vòng lặp"""
for letter in 'Python':     # Vi du thu nhat
   if letter == 'h':
      continue
   print ('Chu cai hien tai :', letter)
var = 10                    # Vi du thu hai
while var > 0:
   var = var -1
   if var == 5:
      continue
   print ('Gia tri bien hien tai la :', var)
print ("Good bye!")

# pass...
"""được sử dụng khi một lệnh là cần thiết theo cú pháp nhưng bạn không muốn bất cứ lệnh hoặc khối code nào được thực thi"""
for letter in 'Python':
   if letter == 'h':
      pass
      print ('Day la khoi pass')
   print ('Chu cai hien tai :', letter)
print ("Good bye!")