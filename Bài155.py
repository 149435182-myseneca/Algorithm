# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 155 - Dinh Quy Pham

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

    def xuLy(self):
        print(self.duyet)
        lstduong = list()
        lstam = list()
        print(f"Giá trị xa {self.n} nhất trong mảng là : ", end="")
        for i in self.duyet:
            if i >= 0:
                tong = i - self.n
                lstduong.append(tong)
            else:
                tong = self.n - i
                lstam.append(tong)
        if len(lstduong) > 0 and len(lstam) == 0:
            ket_qua_duong = max(lstduong) + self.n
            print(ket_qua_duong)
        elif len(lstam) > 0 and len(lstduong) == 0:
            ket_qua_am = -(max(lstam) - self.n)
            print(ket_qua_am)
        else:
            phan_tich = max(lstduong) - max(lstam)
            ket_qua_am = -(max(lstam) - self.n)
            ket_qua_duong = max(lstduong) + self.n
            if phan_tich < 0:
                print(ket_qua_am)
            elif phan_tich > 0:
                print(ket_qua_duong)
            else:
                print(ket_qua_am, "và", ket_qua_duong)

goi = so_Chan(int(input("Nhập n : ")))
goi.nhap()
goi.xuLy()
