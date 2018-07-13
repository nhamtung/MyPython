
# https://vietjack.com/python/assertion_trong_python.jsp

print("Lệnh assert trong Python")
def ChuyenKF(Nhietdo):
   assert (Nhietdo >= 0),"Lanh hon do khong tuyet doi!"
   return ((Nhietdo-273)*1.8)+32

print (ChuyenKF(273))
print (int(ChuyenKF(505.78)))
print (ChuyenKF(-5))