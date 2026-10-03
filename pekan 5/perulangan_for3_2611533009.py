# buat file dengan nama perulangan_for3_NIM.py
# buat program untuk perluangan for dalam Phyton
# nama variable ditambah 4 digit nim terakhir contoh : ulang_3009
# program ini menggunakan fungsi inpjut()

ulang_3009 = int(input("3009: "))

jumlah_3009 = 0
for i_3009 in range(1, ulang_3009 + 1):
    print(i_3009, end=" ")
    jumlah_3009 = jumlah_3009 + i_3009

    if i_3009 < ulang_3009:
        print(" + ", end= " ")
    else:
        print(" = ", jumlah_3009, end="")
        print()
        print("jumlah =", jumlah_3009)