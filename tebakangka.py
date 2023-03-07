import random
a=range(1000000)
print(a)
b=random.choice(a)
i=int(input("Angka:"))
while i!=b:
    print("jawaban anda salah")
    if i>b:
        print('tebakan anda terlalu besar')
    else: print('tebakan anda terlalu kecil')
    i=int(input("Angka:"))
else:print("anda benar Jawabannya adalah",b)