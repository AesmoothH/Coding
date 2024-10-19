import os
import random
import string

data = dict()
while True:
    os.system("cls") # WIN
    print(f" {'DATA AKUN NKAI: STAR RAIL':🫵^45}")
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    akun = input("Enter Nama Akun:\t")
    id = input("Enter ID:\t")
    trailblazer = input("Enter Level TrailBlazer:\t")
    data[ keyFinal ] = { keyFinal : { 'Nama' : akun, 'ID' : id,'TrailBlaze Level' : trailblazer } }
    
    opsi = input("input data LAGI (y/t) :").lower()
    if opsi == 't':
        break

print("-"*40)
print(f"Key\t |Nama Akun|\t |ID|\t |Level Trailblazer|\t")
print("-"*40)
for key, value in data.items():
    print(f"{key}.\t {data[key]}")
