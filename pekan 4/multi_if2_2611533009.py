# Buat file dengan nama multi_if2_2611533009.py
# Buat program untuk kondisional if
# Nama variable ditambahkan 4 digit nim terakhir contoh : total_belanja_3009
# Program ini menggunakan fungsi input()
# Program ini menghitunh total belanja

# Input dari user
total_belanja = float(input("masukkan total belanja (Rp): "))

# input status member (mengecek apakah use mengetik 'y' atau 'ya'
input_member = input("Apakah anda member? (y/t): ").strip().lower()
is_member = input_member in ["y", "ya"]

# input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid = input_promo in ['y', 'ya']

total_diskon_persen = 0

# multi-if terpisah: setiap kondisi diperiksa secara independen
# diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja > 1000000:
    total_diskon_persen += 10 # diskon belanja besar

if is_member:
    total_diskon_persen += 5 # diskon member

if kode_promo_valid:
    total_diskon_persen == 15 # diskon voucher

# menghitung nominal diskon dan total bayar
nominal_diskon = total_belanja * (total_diskon_persen / 100)
total_bayar = total_belanja - nominal_diskon

# output hasil
print("\n--- Rincian Pembayaran---")
print(f"Total Diskon : {total_diskon_persen}% (Rp {nominal_diskon:,.0f})")
print(f"Total Bayar : Rp {total_bayar:,.0f}")

print(f"Total diskon yang anda dapatkan: (total_diskon_persen)%")
# output: total diskon yang anda dapatkan 30% jika belanja > 1 juta, member, dan kode promo valid