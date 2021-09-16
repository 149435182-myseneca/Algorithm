# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 74 - Dinh Quy Pham

n = int(input("Nhập N : "))
x = int(input("Nhập X : "))

giatri = n
tongcuoi = 1 - x
tong = 0
lst1 = list()

def giao_thua(u):
    if u == 0 or u == 1:
        return 1
    else:
        return u * giao_thua(u -1)

for a in range(1,n+1):
    tong = giao_thua(2 * a +1)
    lst1.append(tong)
print(lst1)

for b in range(n):
    rut_gon = 2 * (giatri - b) + 1
    tongcuoi += pow(-1,(giatri-b)+1)*(pow(x,rut_gon) / lst1[(n-1)-b])

print(tongcuoi)




