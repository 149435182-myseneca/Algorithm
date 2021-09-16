# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 41 - Dinh Quy Pham
# Chỉ đúng tới n = 5 vì sau đó máy tính tính sai
n = int(input("Nhập N : "))

lst = list()
for a in range(1):
    x = 1 + 1/(1+1)
    lst.append(x)
    for b in range(n-1):
        print(lst)
        print(lst[b])
        y = 1 + 1/lst[b]
        lst.append(y)
        
print(1/lst[n-2])


