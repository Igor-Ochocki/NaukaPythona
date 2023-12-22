# 8.4. Dla pliku dane.dat obliczyć prędkość w danej chwili v=s/t
# i zapisać do pliku dane1.dat w miejscu prędkości zamiast 0.000000.
# Uwaga na dzielenie przez zero!

dane1 = open("dane1.dat", "w")

with open("dane.dat", "r") as dane:
    for line in dane:
        if line[0] == "#": continue
        data = [float(val) for val in line.split()]
        # data[0] - s
        # data[1] - t
        if data[1] == 0:
            dane1.write(f"{data[0]} {data[1]} Dzielenie przez zero\n")
            continue
        data[2] = data[0] / data[1]
        dane1.write(f"{data[0]} {data[1]} {data[2]}\n")
    dane1.close()
