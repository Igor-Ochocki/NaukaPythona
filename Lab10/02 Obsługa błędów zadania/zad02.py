# Napisz przykładowy kod z obsługą błędów przy podawaniu błędnej daty z klawiatury
# (ponawiamy podawanie daty, aż bedzie poprawna).
# data - dd-mm-rrrr -> ['dd','mm,'rrrr']
while(True):
    try:
        inputData = input("Podaj datę: ")
        dataValues = inputData.split("-")
        if len(dataValues) != 3:
            raise Exception('incorrect date format')
        day = int(dataValues[0])
        month = int(dataValues[1])
        year = int(dataValues[2])
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1 or year > 9999:
            raise Exception('incorrect date values')
        break
    except Exception as e:
        print("Niepoprawna data: ", e)