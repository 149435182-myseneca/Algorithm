# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 104 - Dinh Quy Pham
print("Chương trình nhập vào một số tự nhiên có hai chữ số, và in ra cách đếm chữ số đó")
print("--------------------------------------------------------------------------------")

dic1 = {1: "Một trăm", 2: "Hai trăm", 3: "Ba trăm",
        4: "Bốn trăm", 5: "Năm trăm", 6: "Sáu trăm",
        7: "Bảy trăm", 8: "Tám trăm", 9: "Chín trăm"}

dic2 = {10: "mười", 20: "hai mươi", 30: "ba mươi",
        40: "bốn mươi", 50: "năm mươi", 60: "sáu mươi",
        70: "bảy mươi", 80: "tám mươi", 90: "chín mươi"}

dic3 = {1:"mốt", 2:"hai", 3:"ba",
        4:"bốn", 5:"lăm", 6:"sáu",
        7:"bảy", 8:"tám", 9:"chín"}

# Mở vòng lặp While để lặp lại hành động nếu nhập sai dữ liệu
while True:
     try:
          so = int(input("Nhập vào số N có ba chữ số : "))
          # Gán a là kết quả hàng trăm
          a = so // 100
          # Gán b là kết quả hàng chục
          b = so % 100
          # Gán c là kết quả hàng đơn vị
          c = b % 10
          if 99 < int(so) < 1000:
               if b == 0 and c == 0:
                    print(dic1[a])
               elif b == 11:
                    print(dic1[a], "mười một")
               # Đọc hàng chục
               elif b - c in dic2.keys():
                    # Nếu hàng đơn vị khác 0
                    if c != 0:
                        print(dic1[a], dic2[b - c], dic3[c])
                    # Nếu hàng đơn vị bằng 0
                    else:
                        print(dic1[a], dic2[b - c])
               # Trường hợp kết quả hàng chục = 0
               else:
                    # Nếu hàng đơn vị khác 5 và khác 1
                    if c !=5 and c != 1:
                        print(dic1[a], "lẻ", dic3[c])
                    # Nếu hàng đơn vị bằng 1
                    elif c == 1:
                        print(dic1[a], "lẻ một")
                    # Nếu hàng đơn vị bằng 5
                    else:
                        print(dic1[a], "lẻ năm")
          else:
               print("Số N phải lớn hơn 99 và bé hơn 1000. Hãy nhập lại !")
               # Câu lệnh continue để lặp lại vòng lặp, buộc người dùng phải nhập đúng dữ liệu
               continue
     except ValueError:
          print("Mày có biết viết chữ số không thằng ngu ?")
          continue
     else:
          break





