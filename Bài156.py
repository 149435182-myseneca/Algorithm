# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 156 - Dinh Quy Pham
import numpy

class so_Chan:
    duyet = list()

    def __init__(self,n):
        self.n = n


    def nhap(self):
        while True:
            try:
                check = int(input("Enter : "))
                self.duyet.append(check)
            except ValueError:
                print("Done list !")
                break

    def find_nearest(self):
        self.duyet = numpy.asarray(self.duyet)
        idx = (numpy.abs(self.duyet - self.n)).argmin()
        a = self.duyet[idx]
        print(a)


goi = so_Chan(int(input("Nhập n : ")))
goi.nhap()
goi.find_nearest()
