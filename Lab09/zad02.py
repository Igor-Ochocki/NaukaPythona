# 2. Mamy do despozycji plik baseball.txt
# Należy wyświetlić wszystkich zawodnikaów z drużyny 'OAK'
# Którzy zawodnicy zdobyli największą ilość punktów (pole - run)?
# Którzy zawodnicy zdobyli największą ilość punktów średnio w jednym meczu (run/games)?

#1.  firstname, lastname, age: Informacje personalne o zawodniku, takie jak imię, nazwisko i wiek.
#2.  team: Zespół, do którego zawodnik należy.
#3.  games: Liczba rozegranych przez zawodnika meczów.
#4.  at_bats: Ilość podejść do odbicia, czyli sytuacje, gdy zawodnik próbuje odbić piłkę.
#5.  runs: Ilość zdobytych punktów przez zawodnika po przebiegnięciu bazy.
#6.  hits: Ilość trafionych piłek przez zawodnika.
#7.  doubles: Ilość podwójnych uderzeń, czyli sytuacje, gdy zawodnik osiągnął drugą bazę po swoim uderzeniu.
#8.  triples: Ilość potrójnych uderzeń, czyli sytuacje, gdy zawodnik osiągnął trzecią bazę po swoim uderzeniu.
#9.  homeruns: Ilość home runów, czyli sytuacje, gdy zawodnik uderza piłkę poza granice boiska, zdobywając tym samym punkty.
#10. RBIs (Runs Batted In): Ilość zdobytych punktów przez współzawodnika po uderzeniu danego zawodnika.
#11. walks: Ilość wypraszających, czyli sytuacje, gdy zawodnik dostaje darmowy przejście na pierwszą bazę bez uderzania piłki.
#12. strikeouts: Ilość sytuacji, gdy zawodnik jest wyeliminowany przez rzutnika przeciwnego zespołu.
#13. bat_ave (batting average): Średnia uderzeń, czyli stosunek liczby trafionych uderzeń do liczby podejść do odbicia.
#14. on_base_pct (on-base percentage): Procent osiągania bazy, czyli stosunek sumy liczby trafionych uderzeń, wypraszających i błędów przeciwnika do sumy podeść do odbicia, wypraszających i błędów przeciwnika.
#15. slugging_pct (slugging percentage): Procent zagrywki, czyli stosunek liczby punktów zdobytych dzięki podwójnym, potrójnym i home runom do liczby podeść do odbicia.
#16. stolen_bases: Ilość skradzionych baz przez zawodnika.
#17. caught_stealing: Ilość sytuacji, gdy zawodnik został zatrzymany podczas próby skradzenia bazy przez przeciwnika.


with open("baseball.txt", "r") as dane:
    dane.readline()
    lines = dane.readlines()
    top_runs = []
    top_run = 0
    top_runs_per_games = []
    top_run_per_games = 0
    for line in lines:
        line = line.strip()
        data = line.split(" ")
        final_data = []
        for i in data:
            if i != "":
                final_data.append(i)
        if final_data[3] == "OAK":
            print(f"{final_data[0]} {final_data[1]} {final_data[2]}")

        if int(final_data[6]) > top_run:
            top_run = int(final_data[6])
            top_runs = [f"{final_data[0]} {final_data[1]} {final_data[2]}"]
        elif int(final_data[6]) == top_run:
            top_runs.append(f"{final_data[0]} {final_data[1]} {final_data[2]}")

        if float(final_data[6]) / int(final_data[4]) > top_run_per_games:
            top_run_per_games = float(final_data[6]) / float(final_data[4])
            top_runs_per_games = [f"{final_data[0]} {final_data[1]} {final_data[2]}"]
        elif float(final_data[6]) / int(final_data[4]) == top_run_per_games:
            top_runs_per_games.append(f"{final_data[0]} {final_data[1]} {final_data[2]}")
    print(top_runs)
    print(top_runs_per_games)
