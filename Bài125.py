# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 125 - Dinh Quy Pham
class nhap:
    def __init__(self, n):
        self.n = n

    def xuLy(self):
        for num in range(2, self.n):
            for i in range(2, num):
                if (num % i == 0):
                    break
            else:
                print(num, end="\t")
stde = nhap(int(input("Nhập n : ")))
stde.xuLy()


