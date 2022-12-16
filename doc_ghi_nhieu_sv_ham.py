from student import SinhVien
import os
import pickle

def ghi_sinhvien(thumuc: str, ten_taptin: str, objs: list[SinhVien]):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(objs, f)
        print("Hoàn thành quá trình ghi dữ liệu vào tập tin")
    except Exception as e:
        print(e)
        print("Xảy ra lỗi trong quá trình ghi file")

def doc_sinhvien(thumuc: str, ten_taptin: str) -> list[SinhVien]:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def in_list_sinhvien(content: list[SinhVien]):
    for item in content:
        print(item)

def main():
    path = "D:/data/My Documents/"
    filename = "dulieu.txt"
    sv1 = [SinhVien("Nhat Hieu", 2004, 10.0),
           SinhVien("Thu Thao", 2004, 10.0),
           SinhVien("Minh Khanh", 2004, 10.0)]
    ghi_sinhvien(path, filename, sv1)
    noidung = doc_sinhvien(path, filename)
    in_list_sinhvien(noidung)
    print("Kết thúc chương trình")

if __name__ == "__main__":
    main()