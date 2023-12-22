# app08
# Rzucamy czterema kośćmi aż wyrzucimy cztery szóstki lub cztery jedynki 
# jednocześnie liczymy ile razy losowaliśmy aby zaistniała taka sytuacja.
# Wyświetlamy tylko ilość rzutów oraz informację czy wyrzuculiśmy jedynki czy szóstki 

# Modyfikujemy naszą aplikację aby można rzucać maksymalnie 100 kośćmi - podawanych z klawiatury.
import random

current_rolls = 0
roll_count = 6

while True:
    current_rolls += 1
    roll_sum = 0
    for i in range(roll_count):
        roll_sum += random.randint(1,6)
    if roll_sum == 6 * roll_count or roll_sum == roll_count:
        print(str(current_rolls) + (" 6" if roll_sum == 6 * roll_count else " 1"))
        break