# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 104 - Dinh Quy Pham
nhap_ngay  = int(input("Hãy nhập vào ngày : "))
nhap_thang = int(input("Hãy nhập vào tháng : "))
nhap_nam   = int(input("Hãy nhập vào năm : "))

tinh_ngay = 0
dict1 = {0:0, 1:31, 2:29, 3:31, 4:30,
        5:31, 6:30, 7:31, 8:31,
        9:30, 10:31, 11:30, 12:31}

dict2 = {0:0, 1:31, 2:28, 3:31, 4:30,
        5:31, 6:30, 7:31, 8:31,
        9:30, 10:31, 11:30, 12:31}
# Nhuần 29 ngày
if (nhap_nam % 4 == 0) and (nhap_nam % 100 != 0):
    while nhap_thang > 0:
        if nhap_thang in dict1.keys():
            tinh_ngay += dict1[nhap_thang-1]
            nhap_thang -= 1
else:
    while nhap_thang > 0:
        if nhap_thang in dict2.keys():
            tinh_ngay += dict2[nhap_thang-1]
            nhap_thang -= 1

tinh_ngay += nhap_ngay

print("Ngày bạn nhập là ngày thứ :",tinh_ngay,"Trong năm", nhap_nam)





