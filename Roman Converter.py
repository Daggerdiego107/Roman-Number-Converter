def convert_to_roman(num):
    if not (0 < num < 4000):
        return "Number out of range"
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = ""
    i = 0
    while num > 0:
        its = num // values[i]
        result += symb[i] * its
        num -= values[i] * its
        i += 1
    return result

def valid_num():
    while True:
        inp = input("Type a number between 1 and 3999: ")
        if inp.isdigit():
            num = int(inp)
            if 0 < num < 4000 :
                return num
        print("Please type in a valid number")

num=valid_num()
rom_result=convert_to_roman(num)
print(f"The number {num} converted to Roman is: {rom_result}")