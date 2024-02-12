'''
Write a Python program (using functions) to convert currency
from Canadian currency to four different country's currencies
(Mexico, Brazil, India, UK). Present the menu to the user as follows:

Please enter the number for the country:
1. 1 cad = Mexico 14.56(Peso)
2. 1 cad = Brazil 2.52(Real)
3. 1 cad = India 52.40(Rupee) 
4. 1 cad = UK 0.60(Pound)
'''
def conversion_cad():
    Num = int(input("Please enter a number to select a country's currency: "))
    CAD = float(input("Enter the canadians dollars you intend to convert: "))

    # IF statements for my definitions
    if Num == 1:
        converted = (CAD * 14.56)
        print("The conversion is" ,CAD,"CAD to %.2f"%converted," Peso")

    elif Num == 2:
        converted = (CAD * 2.52)
        print("The conversion is" ,CAD,"CAD to %.2f"%converted," Real")
    elif Num == 3:
        converted = (CAD * 52.40)
        print("The conversion is" ,CAD,"CAD to %.2f"%converted," Rupee")
    elif Num == 4:
        converted = (CAD * 0.60)
        print("The conversion is" ,CAD,"CAD to %.2f"%converted," Pound")
    else:
        print("Invalid input, enter number in the range [1,4] provided")

conversion_cad()





