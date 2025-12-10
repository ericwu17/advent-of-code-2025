# Note: 3017165 too high
# Note: 17577 too high too :(
# Note: 16118 too low!
# correct answer was 17576

import sys
import re
from collections import deque
import numpy as np


from sympy import Matrix

EPSILON = 10**(-3)

def get_num_presses_from_free_vars(free_var_state, m, free_vars, pivots):
    # print("free_var_state: ", free_var_state)
    # print("free_vars: ", free_vars)
    # print("pivots: ", pivots)

    N = len(free_vars) + len(pivots)  # number of buttons
    sol = [0 for _ in range(N)]

    # populate free variables
    for val, i in zip(free_var_state, free_vars):
        sol[i] = val
    
    for index, pivot_idx in enumerate(pivots):
        v = m[index][-1]
        for fv_val, fv_idx in zip(free_var_state, free_vars):
            v += (-1) * fv_val * m[index][fv_idx]
        sol[pivot_idx] = v
    
    # print("candidate sol ", sol)
    # check that everything in the solution is a positive integer
    for v in sol:
        if v < 0 - EPSILON:
            # print("rejecting (negative)")
            return (10**6, None)
        if abs(float(v) - round(v)) > EPSILON:
            # print(f"rejecting (non integer value {v})")
            return (10**6, None)

    sol = [round(x) for x in sol]
    
    # print("accepting")
    return (sum(sol), sol)


def gen_free_var_states(free_vars_maximums):
    if len(free_vars_maximums) == 0:
        yield []
        return

    N = len(free_vars_maximums)
    s = [0 for _ in free_vars_maximums]
    while True:
        yield s
        s[0] += 1
        i = 0
        while s[i] > free_vars_maximums[i]:
            s[i] = 0
            i += 1
            if i >= N: 
                return
            s[i] += 1

def compute_free_var_max(button_wiring, target_state):
    return min(target_state[b] for b in button_wiring)

def solve(target_state, buttons):

    m = np.zeros([len(target_state), len(buttons) + 1])
    for i in range(len(target_state)):
        m[i][-1] = target_state[i]
    for i in range(len(buttons)):
        for b in buttons[i]:
            m[b][i] = 1
    
    # print(m)

    m_rref = Matrix(m).rref()
    m, pivots = m_rref

    free_vars = [i for i in range(len(buttons)) if i not in pivots]
    free_vars_maximums = [compute_free_var_max(buttons[free_var], target_state) for free_var in free_vars]


    m = np.array(m).astype(np.float64)


    # print("MATRIX IN ROW E FORM")
    # print(m)
    # print(pivots)
    # print(free_vars)
    # print(free_vars_maximums)

    min_n_presses = 10**6
    best_sol = None
    # SOLVE NOW. For each free variable, go from 0 up to its max
    for free_var_state in gen_free_var_states(free_vars_maximums):
        (num_pressed, sol) = get_num_presses_from_free_vars(free_var_state, m, free_vars, pivots)
        min_n_presses = min(min_n_presses, num_pressed)

    # print("min number of presses here is ", min_n_presses)
    
    if min_n_presses == 10**6:
        print("ERROR")
        return "ERROR"
    return min_n_presses



count = 0

max_num_buttons = 0
max_state_len = 0

line_no = 0
for line in sys.stdin:
    a, b, c = re.search(r"\[(.*)\] \((.*)\) \{(.*)\}", line.strip()).groups()
    
    # target_state = [c == '#' for c in a]
    buttons = [tuple(map(int, l.split(','))) for l in b.split(") (")]
    target_state = list(map(int, c.split(',')))

    # print(buttons)

    if len(buttons) > max_num_buttons: max_num_buttons = len(buttons)

    if len(target_state) > max_state_len: max_state_len = len(target_state)

    # print(target_state)
    # print(buttons)
    # print(joltage_reqs)
    # print(f"{len(buttons)} buttons and {len(target_state)} places")

    min_pressed = solve(target_state, buttons)
    # print("MIN COUNT IS ", min_pressed)

    count += min_pressed

    print("processed line number ", line_no, " and got min num presses ", min_pressed)
    line_no += 1

print("max number of buttons is ", max_num_buttons)    # up to 13 different buttons                  
print("max length of state is ", max_state_len)        # up to 10 different positions in the state   2**10 = 1024 is manageable.

print("final count is ", count)
