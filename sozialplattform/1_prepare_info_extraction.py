import csv

with open("by-leistung.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()

with open("data/1/infos.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith(">"):
            antragUrl = "https://sozialplattform.de/leistung/" + line[1:]
            infoUrl = "https://sozialplattform.de/inhalt/" + lines[i - 1].strip().split(":")[0].strip()
            leikaId = lines[i + 1].strip()
            writer.writerow([leikaId, antragUrl, infoUrl])
