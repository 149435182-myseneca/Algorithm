# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 136 - Dinh Quy Pham

class so_Chan:
    duyet = list()
    def nhap(self):
        while True:
            try:
                check = int(input("Enter : "))
                self.duyet.append(check)
            except ValueError:
                print("Done list !")
                break


    def xuLy(self):
        print(self.duyet)
        print("Vị trí của số chẵn cuối cùng trong mảng là : ", end="")
        for i in self.duyet[::-1]:
            if i % 2 == 0 :
                print(self.duyet.index(i))
                break

goi = so_Chan()
goi.nhap()
goi.xuLy()