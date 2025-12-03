def is_invalid(i, candidate_length):
    # print(i)
    s = str(i)
    n = len(s)
    num_sections = int(n/candidate_length)
    if n % candidate_length == 0:
        first_section = s[:candidate_length]

        for section_idx in range(1, num_sections):
            section = s[(candidate_length * section_idx):(candidate_length * section_idx) + candidate_length]
            if section != first_section:
                return False
        
        print(f"{i} invalid")
        return True
    return False

with open("2.in") as f:
    ranges = f.read().strip()
    count = 0
    for r in ranges.split(","):
        start, stop = map(int, r.split('-'))
        for i in range(start, stop +1):
            for candidate_length in range(1, int(len(str(i))/2 + 1)):
                if is_invalid(i, candidate_length):
                    count += i
                    break
    
    print(count)