print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_3009 = int(input("Masukkan ukuran skala jam pasir (N): "))


def cetak_batas_3009():
    print("#", end="")
    for k_3009 in range(4 * n_3009 + 5):
        print("=", end="")
    print("#")


def cetak_baris_3009(baris_3009):
    print("| ", end="")
    for k_3009 in range(2 * (n_3009 - baris_3009)):
        print(" ", end="")
    for angka_3009 in range(baris_3009, 0, -1):
        print(angka_3009, end=" ")
    print("<*>", end="")
    for angka_3009 in range(1, baris_3009 + 1):
        print(" " + str(angka_3009), end="")
    for k_3009 in range(2 * (n_3009 - baris_3009)):
        print(" ", end="")
    print(" |")


cetak_batas_3009()

# Fase 1: baris N turun ke 1
for baris_3009 in range(n_3009, 0, -1):
    cetak_baris_3009(baris_3009)

# Fase 2: poros tengah
print("|", end="")
for k_3009 in range(2 * n_3009 + 1):
    print(" ", end="")
print("<*>", end="")
for k_3009 in range(2 * n_3009 + 1):
    print(" ", end="")
print("|")

# Fase 3: baris 1 naik ke N
for baris_3009 in range(1, n_3009 + 1):
    cetak_baris_3009(baris_3009)

cetak_batas_3009()