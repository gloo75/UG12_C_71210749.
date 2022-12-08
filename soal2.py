hitung = input("Masukkan angka : ")

angka = input("Masukkan angka yg dihitung : ")

a = 0

for i in hitung:
    if angka in i:
        a +=1

print(f"angka {angka} muncul sebanyak {a} kali.")