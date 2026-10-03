# buat file dengan nama nested_for1_NIM.py
# buat program untuk perluangan for dalam Phyton
# nama variable ditambah 4 digit nim terakhir contoh : ulang_3009
# program ini menggunakan fungsi input()

batas_3009 = int(input("masukkan nilai batas: "))
for i_3009 in range(1, batas_3009 + 1):
    for j_3009 in range(1, (-1 * i_3009 + batas_3009) + 1):
        print(",", end="")
    print(i_3009)