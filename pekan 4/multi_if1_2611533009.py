# Buat file dengan nama multi_if1_nim.py
# Buat program untuk kondisional if
# Nama variable ditambahkan 4 digit nim terakhir contoh : ipk_3009
# Program ini menggunakan fungsi input()

umur = int(input("input umur anda: "))
sim = input("Apakah anda sudah punya SIM C (y/t): ")[0]

if umur >= 17 and sim == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

if umur >= 17 and sim != 'y' :
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur < 17 and sim == 'y' :
    print("Anda belum boleh cukup umur punya SIM")

if umur < 17 and sim != 'y' :
    print("Anda belum cukup umur bawa motor")