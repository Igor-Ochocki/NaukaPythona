# 2. Konwersja kilometry na mile i odwrotnie.
#    W programie wybieramy w pętli aż podamy poprawny wybór np.
#    'Podaj typ konwersji [km->mile]- 0, [mile->km]- 1'.
#    Na tej podstawie wykonujemy funkcje wcześniej zdefiniowaną
#    km_mile(distance) lub mile_km(distance)

# 1 kilometer = 0.621371192 miles
KM_TO_MILE_RATIO = 0.621371192

def km_mile(distance):
    distance_miles = distance * KM_TO_MILE_RATIO
    print("{} km to {:.2f} mil".format(distance, distance_miles))


def mile_km(distance):
    distance_km = distance / KM_TO_MILE_RATIO
    print("{} mil to {:.2f} km".format(distance, distance_km))


distance = float(input("Podaj odległość : "))

print("Podaj typ konwersji [km->mile]- 0, [mile->km]- 1")
user_input = input()
while user_input != "0" and user_input != "1":
    print("Podaj typ konwersji [km->mile]- 0, [mile->km]- 1")
    user_input = input()

if user_input == "0":
    km_mile(distance)
else:
    mile_km(distance)
