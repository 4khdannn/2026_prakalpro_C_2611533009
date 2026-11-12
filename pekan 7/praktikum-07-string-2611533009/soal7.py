# NAME  : MOH AKHDAN MAHYA ROFIQ
# NIM   : 2611533009
# QUESTION 1
name    = input("Masukkan nama anda: ")
nim1    = input("Masukkan NIM anda: ")

full_name = name
nim = nim1
usn_kampus = (full_name[1:5] + nim[7:11])

print("=" * 30)
print(" " * 10,"STUDENT", " " * 10)
print("=" * 30)
print("Name     :" ,name)
print("NIM      :", nim)
print("Username :", usn_kampus.lower())
print("Intake   : 2026")
print("=" * 30)