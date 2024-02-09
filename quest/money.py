
def main():
    value = int(input("Enter a positive integer < 1000: "))
    print(intName(value))

def intName(number):
    part = number    # the amount that still needs to be converted
    name = " "        # the string representing the amount

    if part >= 100:
        name = digitName(part//100) + " hundred" + " "
        part = part % 100 # remove the hundreds

    if part >= 20:
        name += tensName(part) + " "
        part = part % 10 # remove the tens

    elif part >= 10:
        name += teenName(part) + " "
        part = 0

    if part > 0:
        name += digitName(part)

    return name

def digitName(digit):
    if digit == 1: return "one"
    if digit == 2: return "two"
    if digit == 3: return "three"
    if digit == 4: return "four"
    if digit == 5: return "five"
    if digit == 6: return "six"
    if digit == 7: return "seven"
    if digit == 8: return "eight"
    if digit == 9: return "nine"
    return ""
def teenName(number):
    if number == 10: return "ten"
    if number == 11: return "eleven"
    if number == 12: return "twelve"
    if number == 13: return "thirteen"
    if number == 14: return "fourteen"
    if number == 15: return "fifteen"
    if number == 16: return "sixteen"
    if number == 17: return "seventeen"
    if number == 18: return "eighteen"
    if number == 19: return "nineteen"
    return ""
def tensName(number):
    if number >= 90: return "ninety"
    if number >= 80: return "eighty"
    if number >= 70: return "seventy"
    if number >= 60: return "sixty"
    if number >= 50: return "fifty"
    if number >= 40: return "forty"
    if number >= 30: return "thirty"
    if number >= 20: return "twenty"
    return ""

if __name__=="__main__":
    main()