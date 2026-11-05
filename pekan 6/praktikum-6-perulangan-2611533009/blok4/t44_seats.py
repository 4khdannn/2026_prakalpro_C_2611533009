blocked_seat = int(input())

for row in range(1, 4):
    print("Row", row, end=": ")
    
    # Loop untuk kursi 1 sampai 5
    for seat in range(1, 6):
        if seat == blocked_seat:
            break
        print(seat, end=" ")
        
    print()