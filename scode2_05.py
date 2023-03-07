def ganjil(bawah,atas):
    if bawah<atas:
        for i in range(bawah,atas+1):
            if i%2!=0:
                print(i)
    else :
        for i in range(bawah+1,atas,-1):
            if i%2!=0:
                print(i)

                

# ganjil(10,30)
ganjil(97,82)