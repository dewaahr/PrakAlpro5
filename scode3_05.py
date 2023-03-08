matkul=1
Jumlah_Matkul = int(input("Jumlah Matkul:"))
nilai_siu = 0
list_nilai=[]
while matkul<Jumlah_Matkul+1:
    print(f"Nilai Matkul {matkul}:",end=" ")
    matkul=matkul+1
    nilai=input("")
    nilai.lower()
    if nilai=="a":
        # list_nilai.append(4)
        nilai_siu=nilai_siu+4
    elif nilai=="b":
        # list_nilai.append(3)
        nilai_siu=nilai_siu+3
    elif nilai=="c":
        # list_nilai.append(2)
        nilai_siu=nilai_siu+2
    elif nilai=="d":
        # list_nilai.append(1)
        nilai_siu=nilai_siu+1
# total_nilai=sum(list_nilai)
# print(f"Nilai IPS anda semester ini {total_nilai/Jumlah_Matkul:.2f}")
print(f"Nilai IPS anda semester ini {nilai_siu/Jumlah_Matkul:.2f}")