# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 162 - Dinh Quy Pham
import numpy

class so_Chan:
    duyet = list()

    # def __init__(self,n):
    #     self.n = n


    def nhap(self):
        while True:
            try:
                check = int(input("Enter : "))
                self.duyet.append(check)
            except ValueError:
                print("Done list !")
                break

    def find_nearest(self):
        print(self.duyet)
        for i in range(len(self.duyet)-2):
            if self.duyet[i + 1] == self.duyet[i] * self.duyet[i+2]:
                print(self.duyet[i + 1])
                break
        else:
            print("Nothing !")




goi = so_Chan()
goi.nhap()
goi.find_nearest()
