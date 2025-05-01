import random

def make_uchr(code: str):
    return chr(int(code.lstrip("U+").zfill(8), 16))
def rand_dice():
    for i in range(6):
        num = str(random.randrange(2680, 2685))
        print(make_uchr(f"U+{num}"))
rand_dice()