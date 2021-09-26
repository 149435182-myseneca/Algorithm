# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 144 - Dinh Quy Pham

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
        print("Số nguyên tố đầu tiên trong mảng là : ", end="")
        for i in self.duyet:
            prime = True
            for b in range(2,i):
                if i % b == 0:
                    prime = False
            if prime:
                print(i)
                break
goi = so_Chan()
goi.nhap()
goi.xuLy()