
def perkalian(a, b):
    proses = 0
    b_list=[b]
    for i in range(a-1):
        b_list.append(b)
        hasil=a*b
    print(a,"x",b,end=" = ")
    print (*b_list,sep=" + ",end=" = ")
    print (hasil)
    
perkalian(6,5)
perkalian(7,10)
perkalian(9,9)