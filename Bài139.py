# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 139 - Dinh Quy Pham

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
        print("Vị trí của số hoàn thiện cuối cùng là : ", end="")
        for i in self.duyet[::-1]:
            # Tạo list lst để bắt lại ước của những số trong danh sách duyet
            lst = list()
            tong = 0
            for a in range(1,i):
                if i % a == 0:
                    lst.append(a)

            # Duyệt các ước của i sau đó cộng lại
            for b in lst:
                tong += b
            # Nếu tổng == i đó là số hoàn thiện
            if tong == i:
                print(self.duyet.index(i))
                break

goi = so_Chan()
goi.nhap()
goi.xuLy()