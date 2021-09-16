# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 42 - Dinh Quy Pham
n = int(input("Nhập N : "))
tong = 0
lst = list()
for x in range(n):
    tong += x
    if tong < n:
        lst.append(x)
        a = max(lst)
print(a)



