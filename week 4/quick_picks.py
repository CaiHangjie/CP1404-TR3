import random

MIN_QUICK_PICK_NUMBER = 1
MAX_QUICK_PICK_NUMBER = 45
NUMBERS_IN_A_PICK = 6

quick_picks = int(input("How many quick picks? "))

for i in range(quick_picks):
    quick_pick = []
    while len(quick_pick) < NUMBERS_IN_A_PICK:
        random_number = random.randint(MIN_QUICK_PICK_NUMBER, MAX_QUICK_PICK_NUMBER)
        if random_number not in quick_pick:
            quick_pick.append(random_number)
    quick_pick.sort()
    print(" ".join(f"{n:2}" for n in quick_pick))
