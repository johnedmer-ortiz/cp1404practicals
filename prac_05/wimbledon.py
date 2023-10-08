lines = []

with open("wimbledon.csv", encoding="utf-8-sig") as in_file:
    for line in in_file:
        lines.append(line.split(","))
