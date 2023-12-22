# 3. Konwersja stopni Celsjusza na Fahrenheita i odwrotnie (funkcja)
#    convert_temp(type, value) gdzie type ma wartości małe lub duże 'F' or 'C'
#  °F =°C * 1.8000+ 32.00
# F - 32 = C * 1.8
# (F - 32) / 1.8 = C
C_TO_F_RATIO = 1.8
C_TO_F_CONST = 32

def convert_temp(type, value):
    if(type == 'F'):
        print("Temperatura wynosi: {:.2f}F".format(value * C_TO_F_RATIO + C_TO_F_CONST))
    else:
        print("Temperatura wynosi: {:.2f}C".format((value - C_TO_F_CONST) / C_TO_F_RATIO))


temperature = float(input("Podaj wartość temperatury: "))

user_input = input("Podaj konwersję: (C lub F) ").upper()
if user_input == "C" or user_input == "F":
    convert_temp(user_input, temperature)
else:
    print("Nieprawidłowa operacja")
# while user_input != "C" and user_input != "F":
#     user_input = input("Podaj konwersję: (C lub F) ")
# convert_temp(user_input, temperature)

