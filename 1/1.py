with open("./1.in") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]


pos = 50
pw = 0

for line in lines:
    prev_pos = pos

    if line.startswith("R"):
        for _ in range(int(line[1:])):
            pos += 1
            if pos == 100: pos = 0
            if pos == 0: pw += 1
    else:
        for _ in range(int(line[1:])):
            pos -= 1
            if pos == -1: pos = 99
            if pos == 0: pw += 1

    
    

print(pw)