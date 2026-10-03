# buat file dengan nama perulangan_for2_NIM.py
# buat program untuk perluangan for dalam Phyton
# nama variable ditambah 4 digit nim terakhir contoh : ulang_3009
# program ini menggunakan fungsi inpjut()

ulang_3009 = int(input("Masukkan jumlah perulangan: "))
print("perulangan ke-0 sampai ke-", ulang_3009-1)
for i_3009 in range(ulang_3009):
    print(i_3009, end="")
print()
print("perulangan ke-1 sampai ke-", ulang_3009)
for i_3009 in range(1, ulang_3009+1):
    print(i_3009, end=" ")