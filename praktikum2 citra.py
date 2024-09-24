# Python file   : Praktikum 2 PTI
# author        : Zaskiana Citra Nainggolan

# 1. Variabel Declaration

variabel1 = 10
variabel2 = 10.5
variabel3 = "Sepuluh"
variabel4 = True

# 2. Operators -> + -, *, /,% , =

# 3. Perulangan -> Looping
    # for statement
    # index data -> dimulai 0

for baris in range(5):
    for kolom in range(4):
        print("*",end="")
    print()

print("=============")

# While -> Need Condition

baris2 = 0
tengah = 5
while baris2 < 5:
    kolom2 = 0
    if(baris2 % 2 == 1):
        while kolom2 < 5:
            if(kolom2 == int(round(tengah/2))):
                print("*",end="")
            else:
                print(" ",end="")
            kolom2 += 1
    else:
        while kolom2 < 5:
            print("*",end="")
            kolom2 += 1
    print()
    baris2 += 1



        














