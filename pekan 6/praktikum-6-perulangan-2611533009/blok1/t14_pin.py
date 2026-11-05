correct_pin = "1234"
attemps = 1
MAX_ATTEMPS = 3
pin = input("Enter your PIN: ")
while pin != correct_pin and attemps < MAX_ATTEMPS:
    attemps += 1
    print("Incorrect PIN.")
    pin = input("Enter your PIN: ")

if pin == correct_pin:
    print("Access granted")
else:
    print("Account locked")