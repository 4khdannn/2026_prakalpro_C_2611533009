# buat file dengan nama nested_for4_NIM.py
# buat program untuk perluangan for dalam Phyton
# nama variable ditambah 4 digit nim terakhir contoh : ulang_3009
# program ini menggunakan fungsi input()

tinggi_3009 = int(input("masukkan tinggi pola(bilangan genap, misal 10): "))

if tinggi_3009 % 2 != 0:
    print("tinggi harus bilangan genap")
else:
    a_3009 = tinggi_3009
    c_3009 = a_3009
    lebar_3009 = (2 * tinggi_3009) - 2

    for i_3009 in range(1, tinggi_3009 + 1):
        b_3009 = c_3009 + 1

        for j_3009 in range(1, lebar_3009 + 1):

            # baris atas dan bawah
            if i_3009 == 1 or i_3009 == tinggi_3009:
                if j_3009 == 1 or j_3009 == lebar_3009:
                    print("#", end="")
                else:
                    print("=", end="")

                    # baris isi
            else:
                if j_3009 == 1 or j_3009 == lebar_3009:
                    print("|", end="")
                else:
                    if j_3009 == c_3009:
                        print("<", end="")
                    elif j_3009 == b_3009:
                        print(">", end="")
                    elif j_3009 == (lebar_3009 - c_3009):
                        print("<", end="")
                    elif j_3009 == (lebar_3009 - c_3009 + 1):
                        print(">", end="")
                    elif j_3009 > b_3009 and j_3009 < (lebar_3009 - c_3009 + 1):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # logika asli java
        a_3009 -= 2

        if a_3009 <= 0:
            c_3009 = (-a_3009) + 2
        else:
            c_3009 = a_3009