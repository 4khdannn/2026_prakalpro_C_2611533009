# buat program deengan nama if_elif1_nim.py
# buat program untuk kondisional if
# nama variable ditambah 4 digit nim terakhir contoh: ipk_3009
# program ini menggunakan fungsi input()

umur = int(input("input umur anda: "))
sim = input("Apakah anda sudah punya SIM C (y/t): ")[0]

if umur >= 17 and sim == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

elif umur >= 17 and sim != 'y' :
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

elif umur < 17 and sim == 'y' :
    print("Anda belum boleh cukup umur punya SIM")

else:
    print("Anda belum cukup umur bawa motor")
print("Program selesai")