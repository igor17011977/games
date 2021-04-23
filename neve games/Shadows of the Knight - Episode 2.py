import sys
import math
import numpy as np
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
lp1 = []
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
# z=0
lp = np.array([0])
window = []
n = int(input())  # maximum number of turns before game over.
old_w, old_h = [int(i) for i in input().split()]
window_position = h // 2, w // 2


# game loop
def distance(h1, w1, old_h1, old_w1):
    zp, dp = [], []

    for h2, w2 in lp:
        zxc = np.array([h2, w2])
        zp.append(np.linalg.norm(zxc - [h1, w1]))
        dp.append(math.sqrt(sum([(old_h1 - h2) ** 2 + (old_w1 - w2) ** 2])))
    return [np.array(zp, float), np.array(dp, float)]


# расчет центральной точки следующего прышка

# print("i===final",position,"distans==",b, file=sys.stderr, flush=True)

while True:
    bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
    print("bomb_dir==", bomb_dir, "old===", old_h, old_w, file=sys.stderr, flush=True)
    if bomb_dir == "UNKNOWN":
        print(w // 2, h // 2)
        line_w = list(map((lambda x: x), range(w)))
        for i in range(h): lp1 += list(zip([i] * w, line_w))

        print("a=", lp1, file=sys.stderr, flush=True)

        # lp=np.array([[x, y] for x in range(h) for y in range(w)])
        lp = np.array(lp1)
        continue
    new_position_matrix, old_position_matrix = distance(window_position[0], window_position[1], old_h,
                                                        old_w)  # window_position[0]=h

    old_h, old_w = window_position
    lp = {"WARMER": lambda: lp[new_position_matrix < old_position_matrix],
          "COLDER": lambda: lp[new_position_matrix > old_position_matrix],
          "SAME": lambda: lp[new_position_matrix == old_position_matrix], }[bomb_dir]()
    # print (lp,file=sys.stderr, flush=True)

    window = lp.tolist()
    # print("windown11==.",window, file=sys.stderr, flush=True)

    if [old_h, old_w] in window: window.remove([old_h, old_w])

    vb_h = {*map(lambda x: x[0], window)}
    z_h = list(vb_h)
    print("z_h==.", z_h, file=sys.stderr, flush=True)
    vb_h = z_h[len(z_h) // 2]
    print("vb_h==.", vb_h, file=sys.stderr, flush=True)
    vb_w = [x[1] for x in window if x[0] == vb_h]

    print("vb_w==.", vb_w, file=sys.stderr, flush=True)
    vb_w = vb_w[len(vb_w) // 2]

    # print("window_position==.",z_h, file=sys.stderr, flush=True)
    window_position = [vb_h, vb_w]
    # window_position = window[len(window)//2]

    print("window_position==.", window_position, file=sys.stderr, flush=True)

    window.remove(window_position)
    lp = np.array(window)

    print(window_position[1], window_position[0])