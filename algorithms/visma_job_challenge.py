# notes:
# brute force.
# word search for 31203 = ?, then check for the rest of the letters. bedre enn vanlig brute force.
# plus from the right side? extra number is max 3.

"""
find what value each letter represents, given the following equation:
VISMA + API + AI SAAS = HEAVEN

Every letter shall be assigned a unique base-10 digit value.
So, {V, I, S, M, A, P, H, E, N, L} = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
but, A != 1, and M != 2
"""
from itertools import permutations
import time


VISMA = "VISMA"
API = "API"
AI = "AI"
SAAS = "SAAS"
HEAVEN = "HEAVEN"

letters_in = "VISMAPHENL"
num_out = "0123456789"

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
start_time = time.time()
for combo in permutations(lst, 10):
    if combo[4] == 1 or combo[3] == 2:
        continue

    # cast to string and put in a list
    num_out = [str(x) for x in combo]
    trans = VISMA.maketrans(letters_in, "".join(num_out))

    # translate and cast to int for each word
    word1 = int(VISMA.translate(trans))
    word2 = int(API.translate(trans))
    word3 = int(AI.translate(trans))
    word4 = int(SAAS.translate(trans))
    eq = int(HEAVEN.translate(trans))

    if word1 + word4 + word3 + word2 == eq:
        stop_time = time.time()
        print(d := dict(zip(num_out, [*letters_in])))
        print()
        print("31203 = ", d["3"] + d["1"] + d["2"] + d["0"] + d["3"])
        print("It took:", stop_time - start_time, "seconds :)")
        break

# i can check by multiplying each letter occurrence by 1, 10, 100, 1000, etc.
# or i can make strings and convert to int, then check. i chose this second option. using strings
