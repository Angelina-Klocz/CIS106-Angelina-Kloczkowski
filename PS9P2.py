def square_footage(l, w, h):
    return 2*l*w + 2*l*h + 2*w*h

while input("Run program? (Yes/No): ").lower() == "yes":
    length = float(input("Length: "))
    width = float(input("Width: "))
    height = float(input("Height: "))

    area = square_footage(length, width, height)
    gallons = area / 50

    print("Gallons needed:", gallons)