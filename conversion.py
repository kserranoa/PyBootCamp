#Convert farenheit to celsius
def toCelsius():
    farenheit = int(input("Enter farenheit\n >>> "))
    formula = (farenheit-32) * 5/9
    return formula
