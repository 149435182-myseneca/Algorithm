# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 67 - Dinh Quy Pham

n = int(input("Nhập N : "))
x = int(input("Nhập X : "))

giatri = n
tongcuoi = 0
tong = 0

for a in range(n):
    tongcuoi += pow(-1,(giatri-a)+1)*pow(x,(giatri-a))
print(tongcuoi)




