def get_max_pot_j(joltages, n):
    if n == 1:
        return max(joltages)

    l = len(joltages)
    for first_digit in (9,8,7,6,5,4,3,2,1):
        for i in range(0, l - (n-1)):
            if joltages[i] == first_digit:
                multiplier = 10**(n-1)
                return multiplier * joltages[i] + get_max_pot_j(joltages[i+1:], n-1)


with open("in.txt") as f:
    total_max_joltage = 0
    for line in f.readlines():
        line = line.strip()
        joltages = []
        for c in line:
            joltages.append(c)
        joltages = [int(j) for j in joltages]
        
        n = len(joltages)
        total_max_joltage += get_max_pot_j(joltages, 12)

print(total_max_joltage)