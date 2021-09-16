# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 19 - Dinh Quy Pham
n = int(input("Nhập N : "))
x = int(input("Nhập X : "))

tong = 1
lst = list()

def giai_thua(y):
    if y == 0 or y == 1:
        return 1
    else:
        return y * giai_thua(y-1)
# Mục đích là đưa i vô list lst để vòng lặp b lấy ra dùng
for a in range(n+1):
    i = 2 * a + 1
    lst.append(i)
    for b in range(1):
        tong += pow(x,lst[a])/giai_thua(lst[a])

print(tong)




