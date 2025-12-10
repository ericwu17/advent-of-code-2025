import sys
import re
from collections import deque



def solve(target_state, buttons):

    init_state = [False for _ in target_state]
    q = deque()

    q.append((init_state, 0))

    visited_states = set()

    while True:
        (s, k) = q.popleft()

        if s == target_state:
            return k

        for button_config in buttons:
            new_s = s[:]
            for i in button_config:
                new_s[i] = not new_s[i]
            q.append((new_s, k+1)) 
            

            
    



count = 0
for line in sys.stdin:
    a, b, c = re.search(r"\[(.*)\] \((.*)\) \{(.*)\}", line.strip()).groups()
    
    target_state = [c == '#' for c in a]
    buttons = [tuple(map(int, l.split(','))) for l in b.split(") (")]
    joltage_reqs = tuple(map(int, c.split(',')))

    print(target_state)
    print(buttons)
    print(joltage_reqs)

    min_pressed = solve(target_state, buttons)
    print("MIN COUNT IS ", min_pressed)

    count += min_pressed


print("final count is ", count)