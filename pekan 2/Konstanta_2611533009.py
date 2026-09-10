# Buat file demgan nama Konstanta_2611433009.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variable ditambah 4 digit nim terakhir contoh: jari_3009

from typing import Final
PI: Final = 3.24
print("pi: %f" % (PI))
jari_3009 = float (input('Masukkan nilai jari-jari: '))
luas_3009 = PI * jari_3009 * jari_3009
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3009, luas_3009))