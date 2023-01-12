print("==============Program Konversi Nilai=======================")
while True:
    nilai = input("Masukan Nilai MID: ")
    try:
        inpMid = int(nilai)
        if inpMid >=0  and inpMid <=100:
            break
        else:
            print("inputan harus integer positif")
            continue
    except ValueError:
        print("Nilai Inputan harus integer")
        continue

while True:
    nilai = input("Masukan Nilai UAS: ")
    try:
        inpUas = int(nilai)
        if inpUas >=0  and inpUas <=100:
            break
        else:
            print("inputan harus integer positif")
            continue
    except ValueError:
        print("Nilai Inputan harus integer")
        continue

while True:
    nilai = input("Masukan Nilai Tugas: ")
    try:
        inpTugas = int(nilai)
        if inpTugas >=0  and inpTugas <=100:
            break
        else:
            print("inputan harus integer positif")
            continue
    except ValueError:
        print("Nilai Inputan harus integer")
        continue

while True:
    nilai = input("Masukan Nilai Responsi: ")
    try:
        inpResponsi = int(nilai)
        if inpResponsi >=0  and inpResponsi <=100:
            break
        else:
            print("inputan harus integer positif")
            continue
    except ValueError:
        print("Nilai Inputan harus integer")
        continue
    
mid = 0.25*inpMid
uas = 0.3*inpUas
tugas = 0.3*inpTugas
responsi = 0.15*inpResponsi

total = mid+uas+tugas+responsi
print("Nilai Akhir : ",total)

if total>=0 and total <50:
    print("Nilai Huruf D")
elif  total>=50 and total<65:
    print("Nilai Huruf C")
elif total>=65 and total<80:
    print("Nilai Huruf B")
elif total>=80 and total<=100:
    print("Nilai Huruf A")
print("===========================================================")
