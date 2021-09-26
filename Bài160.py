# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài <160 tương tự cách làm - Dinh Quy Pham

class so_Chan:
    duyet = list()
    def __init__(self,a, b):
        self.a = a
        self.b = b

    def nhap(self):
        while True:
            try:
                check = int(input("Enter phần tử mảng: "))
                self.duyet.append(check)
            except ValueError:
                print("Done list !")
                break

    def xuLy(self):
        print(self.duyet)
        self.duyet.sort()
        lst1 = list()
        lst2 = list()
        for x in self.duyet:
            if x >= self.a :
                lst1.append(x)
        for y in self.duyet:
            if y <= self.b :
                lst2.append(y)

        list1_as_set = set(lst1)
        intersection = list1_as_set.intersection(lst2)

        intersection_as_list = list(intersection)
        print(intersection_as_list)
goi = so_Chan(int(input("Nhập a : ")),
            int(input("Nhập b : ")))
goi.nhap()
goi.xuLy()
