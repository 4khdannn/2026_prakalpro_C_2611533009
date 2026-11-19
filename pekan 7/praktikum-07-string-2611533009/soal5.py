# NAME  : MOH AKHDAN MAHYA ROFIQ
# NIM   : 2611533009

# QUESTION A
username = input("Username: ")

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")

# QUESTION B
nim = input("NIM: ")

if len(nim) < 10:
    print("Invalid: at least 10 digits")
elif not nim.isdigit():
    print("Invalid: digits only")
else:
    print("20", nim[0 : 2])