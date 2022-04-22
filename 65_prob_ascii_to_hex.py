str1 = input("Enter a String: ")


for i in str1:
    ascii_values = ord(i)
    part = hex(ascii_values).lstrip("0x").rstrip("L")


print(ascii_values,part)