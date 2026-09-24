# Buat file dengan nama if1_nim.py
# Buat program untuk kondisional if
# Nama variable ditambahkan 4 digit nim terakhir contoh : ipk_3009
# Program ini menggunakan fungsi input()

ipk = float(input("input IPK Anda"))

if ipk > 2.75:
    print("Anda Lulus Sangat Memuaskan dengan IPK " + str(ipk))
else:
    print("Anda Tidak Lulus")
print("Program Selesai")