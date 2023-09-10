def shakkilauta(kertaa):
    mjono1 = "10" * 1000
    mjono2 = "01" * 1000
    alku = 0
    loppu = kertaa
    i = 1
    # for i in range(1, kertaa + 1):
    while i <= kertaa:
            if i % 2 == 0:
                print(mjono2[alku:loppu]) #parillinen
            else:            
                print(mjono1[alku:loppu]) #pariton
            i += 1    

if __name__ == "__main__":
    shakkilauta(3)
    print()
    shakkilauta(6)
    print()
    shakkilauta(4)